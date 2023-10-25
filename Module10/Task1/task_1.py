print('Задача 1. Имена 2\n')

count = 0
line_num = 0
with open('people.txt', 'r', encoding='utf8') as file:
    for line in file:
        try:
            line_num += 1
            clear_line_len = len(line.rstrip())
            count += clear_line_len
            if clear_line_len < 3:
                raise Exception
        except Exception:
            print(f'Ошибка: менее трёх символов в строке {line_num}')

print(f'Общее количество символов: {count}')