import os
from typing import Union

import cv2
import pickle
import face_recognition


# Обнаружение лиц в видео потоке
def discovery_face(frame, face_cascade):
    return face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=2.0, minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)


# Конвертирует из формата bgr в rgb
def rgb(frame):
    return face_recognition.face_encodings(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


# Запуск стрима
def start_stream(video_path: Union[str, int], path_file_en: str):
    # найти путь к файлу xml, содержащему файл haarcascade
    path_face_cascad = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    # загрузить harcaascade в каскадный классификатор
    face_cascade = cv2.CascadeClassifier(path_face_cascad)
    # загрузить известные лица и вложения, сохраненные в последнем файле
    data = pickle.loads(open(path_file_en, 'rb').read())

    video_capture = cv2.VideoCapture(video_path)
    # зацикливаемся на кадрах из потока видеофайла
    while True:

        # захватить кадр из потокового видеопотока
        ret, frame = video_capture.read()
        faces = discovery_face(frame, face_cascade)
        print(faces)
        encodings = rgb(frame)
        names = list()
        # цикл по лицевым вложениям incase
        for encoding in encodings:
            # Сравните кодировки с кодировками в data["encodings"]
            # Совпадения содержат массив с логическими значениями и значением True для встраивания,
            # которое близко соответствует и False для остальных

            matches = face_recognition.compare_faces(data["encodings"], encoding)

            # set name =unknown, если ни одна кодировка не совпадает
            name = "Unknown"
            # проверяем, нашли ли мы совпадение
            if True in matches:
                # Находим позиции, в которых получаем True и сохраняем их
                matched_idxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                # цикл по совпадающим индексам и сохранение количества для каждого распознанного лица
                for i in matched_idxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                name = max(counts, key=counts.get)

            names.append(name)

            # loop over the recognized faces
            for ((x, y, w, h), name) in zip(faces, names):
                print((x, y, w, h))
                # масштабируем координаты лица
                # нарисовать предсказанное имя лица на изображении
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (0, 255, 0), 2)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
