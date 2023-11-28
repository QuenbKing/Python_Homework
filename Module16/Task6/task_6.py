from LoggerDecorator import LoggerDecorator

print('Задача 6. Класс-декоратор\n')


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    res = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                res += i + j
    return res


result = complex_algorithm(10, 50)
