print('Задание 8. Бегущая строка\n')

first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
if len(first_str) != len(second_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
else:
    for offset in range(1, len(first_str)):
        if second_str == first_str[offset:] + first_str[:offset]:
            print(f'Первая строка получается из второй со сдвигом {offset}')
            break
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига')