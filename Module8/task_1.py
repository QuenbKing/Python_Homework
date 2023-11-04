print('Задача 1. Challenge-2\n')


def get_nums(number):
    if number != 1:
        get_nums(number - 1)
    print(number)


num = int(input('Введите num: '))
get_nums(num)
