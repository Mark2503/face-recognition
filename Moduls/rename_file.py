import os

from transliterate import translit


def rename_file(path: str, file: str, language: str = 'ru'):

    try:
        name = os.path.splitext(file)
        new_name: str = translit(name[0], language_code=language, reversed=True)
        old_path = f'{path}/{file}'
        new_path = fr'{path}\{new_name}' + name[1]
        os.rename(old_path, new_path)
        print(f'{old_path}  ->  {new_path}')
        return new_path

    except Exception as e:
        print(e)
