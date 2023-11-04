import random

summ = 0
try:
    with open("out-file.txt", "w", encoding="utf8") as out_file:
        while summ < 777:
            num = int(input('Введите число: '))
            unlucky_num = random.randint(1, 13)
            stop_num = 7
            if unlucky_num == stop_num:
                raise Exception
            summ += num
            out_file.write(f'{num}\n')
except Exception:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
