print('Задача 2. Дзен Пайтона\n')

zen_file = open('zen.txt', 'r', encoding='UTF-8')
reverse_file_lines_list = zen_file.readlines()[::-1]
reverse_file_lines_list.insert(1, '\n')
reverse_file_lines = ''.join(reverse_file_lines_list)
print(f'Строки файла в обратном порядке:\n{reverse_file_lines}')