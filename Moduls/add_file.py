import os

# from Moduls.rename_file import rename_file


# Добавление в список найденных путей к изображениям с лицами людей
def add_foto_faces_list() -> list:
    """
    :return:
    """
    # return [fr'{root.split(fr"{os.getcwd()}/")[1]}\{file}' for root, dirs,
    # files in os.walk(fr'{os.getcwd()}/Data\fotofaces') for file in files]
    return [fr'{root}\{file}' for root, dirs, files in os.walk(fr'{os.getcwd()}/Data\fotofaces') for file in files]


# Функция генерирует словарь с путями к файлам haarcascade
def add_haarcascade_file() -> dict:
    """
    :return:
    """
    return {
        file: f'{root}/{file}'
        for root, dirs, files in os.walk(fr'{os.getcwd()}/Data/')
        for file in files if file.endswith('xml')
    }








































