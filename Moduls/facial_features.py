import os

import pickle
import cv2
import face_recognition

from Moduls.add_file import add_foto_faces_list


# Срезает имя файла от пути и от расширения файла возвращая чисто имя
def split_file_name(img_path: str) -> str:
    return os.path.splitext(os.path.split(img_path)[1])[0]


# Чтение изображения и конвертирование из BGR в RGB формат
def rgb(img_path: str):
    return cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)


# Обнаружение лиц и вычисление эмбеддинга для каждого лица
def recognitions(rgb_img):

    # используем библиотеку Face_recognition для обнаружения лиц
    boxes = face_recognition.face_locations(rgb_img, model='hog')

    # вычисляем эмбеддинги для каждого лица и возвращаем значение
    return face_recognition.face_encodings(rgb_img, boxes)


# Записывает в файл кодировку эмбеддинга лиц и имена людей с названия изображения
def write_encoding(path: str, data: dict):

    with open(path, 'wb') as file:
        file.write(pickle.dumps(data))
    return path


# Функция анализирует лицо на фото и сохраняет эмбеддинги лица
def facial_features(name_file_face_encoding: str = 'face_en'):

    path_name_file_face_encoding: str = f'{os.getcwd()}/{name_file_face_encoding}'

    # Список где будут храниться кодировки эмбеддинга для каждого лица known_encoding
    # Список где будут храниться имена людей взятые с названия изображения known_name
    known_encoding, known_name = list(), list()

    # перебираем все папки с изображениями
    for (i, img_path) in enumerate(add_foto_faces_list()):

        # извлекаем имя человека из названия изображения
        name: str = split_file_name(img_path)

        for encoding in recognitions(rgb(img_path)):
            known_encoding.append(encoding)
            known_name.append(name)

    return write_encoding(path_name_file_face_encoding, {"encodings": known_encoding, "names": known_name})


