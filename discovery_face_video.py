import os
from typing import Union

import cv2


# Функция чтения видео
def video(video_path):
    return cv2.VideoCapture(video_path)


# Функция обнаружение лиц
def discovery_face(face_cascade, frame):
    return face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(5, 5),
                                         flags=cv2.CASCADE_SCALE_IMAGE
                                         )


# Запуск стрима видео
def start_stream(video_path: Union[str, int] = 0) -> None:
    # найти путь к файлу xml, содержащему файл haarcascade
    path_face_cascad = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"

    # загрузить harcaascade в каскадный классификатор
    face_cascade = cv2.CascadeClassifier(path_face_cascad)

    # зацикливаемся на кадрах из потока видеофайла
    data = video(video_path)
    while True:

        # захватить кадр из потокового видеопотока
        ret, frame = data.read()

        result = discovery_face(face_cascade, frame)

        # Перебираем обнаруженные лица
        for (x, y, w, h) in result:
            # масштабируем координаты лица
            # нарисовать предсказанное имя лица на изображении
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 8)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    data.release()
    cv2.destroyAllWindows()
