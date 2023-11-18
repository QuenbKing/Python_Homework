from Square import Square

print('Задача 1. Квадраты чисел\n')


def get_nums_square(count):
    for num in range(1, count + 1):
        yield num ** 2


class_iterator = Square(10)
generator = get_nums_square(10)
square_nums = (num ** 2 for num in range(1, 11))

for my_num in class_iterator:
    print(my_num)
print()

for my_num in generator:
    print(my_num)
print()

for my_num in square_nums:
    print(my_num)
