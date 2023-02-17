import os

import cv2


# Функция конвертирует изображение в серей цвет
def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Функция обнаруживает лица на изображении
def detected_multiscale(face_cascade, gray):
    return face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )


# Функция запускает обнаружение лиц на изображении
def start(image_path):
    path_face_cascad = os.path.dirname(cv2.__file__) + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(path_face_cascad)

    image = cv2.imread(image_path)
    faces = detected_multiscale(convert_gray(image), face_cascade)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Frame", image)
    cv2.waitKey(0)


start('путь/к/изображению')
