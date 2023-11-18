from collections.abc import Iterable

print('Задача 5. Обработка логов\n')


def error_generator(file_path: str) -> Iterable[str]:
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


with open('errors.txt', 'w') as error_file:
    for error in error_generator('logs.txt'):
        error_file.write(error)
