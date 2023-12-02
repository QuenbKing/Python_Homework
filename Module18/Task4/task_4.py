import re

print('Задача 4. Телефонные номера\n')

phone_numbers = ['9999999999', '999999-999', '99999x9999', '5894732891', '8734267424', '9999A9999', 'A999999999']


def check_numbers(phone_list):
    for num_index in range(len(phone_list)):
        result = re.search(r'\b[89]\d{9}\b', phone_numbers[num_index])
        if result is None:
            print(f'{num_index + 1} номер: не подходит')
        else:
            print(f'{num_index + 1} номер: всё в порядке')


check_numbers(phone_numbers)
