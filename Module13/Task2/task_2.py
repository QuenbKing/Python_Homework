import os.path

print('Задача 2. Пути файлов\n')


def gen_files_path(path: str = os.path.join('..')) -> list[str]:
    result = list()
    for root, dirs, files in os.walk(path):
        result.extend([os.path.join(root, file_name) for file_name in files])
    return result


print(gen_files_path())

user_path = input('Укажите путь до каталога: ')
print(gen_files_path(user_path))
