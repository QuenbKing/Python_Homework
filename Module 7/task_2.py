import math

print('Задача 2. Универсальная программа\n')


def crypto(collection):
    return [item for index, item in enumerate(collection) if index not in [0, 1] and is_prime(index)]


def is_prime(num):
    for divider in range(2, int(math.sqrt(num)) + 1):
        if num % divider == 0:
            return False
    return True


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
