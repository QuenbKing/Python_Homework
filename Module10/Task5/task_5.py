print('Задача 5. Надёжные вычисления\n')


def get_square(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError(f'The number must be greater than zero. Your num: {num}')
        num = num ** 0.5
    except ValueError as exc:
        return exc
    else:
        return num


user_num = input('Введите число: ')
print(get_square(user_num))
