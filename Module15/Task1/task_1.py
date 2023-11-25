from FileContextManager import File

print('Задача 1. Работа с файлом 2\n')

with File('task_file.txt', 'a') as file:
    ''' Автоматическое создание файла в режиме write при отсутствии данного файла'''
    file.write('Привет, я только что создал это файл в режиме write\n')

with File('task_file.txt', 'a') as file:
    file.write('Файл был найден')

with File('task_file.txt', 'r') as file:
    ''' Подавление ошибки записи, при файле открытом для чтения'''
    file.write('Ошибка')

