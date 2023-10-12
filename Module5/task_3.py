print('Задание 3. Файлы\n')

file_name = input('Название файла: ')
start = ('@', '№', '$', '%', '^', '&', '*', '()')
end = ('.txt', '.docx')

if file_name.startswith(start):
    print('Ошибка: название начинается недопустимым символом.')
elif not file_name.endswith(end):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')