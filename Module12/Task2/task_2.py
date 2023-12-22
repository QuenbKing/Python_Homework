import random
from MyExceptions import *

print('Задача 2. Карма\n')


def one_day():
    random_num = random.randint(1, 10)
    if random_num == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error
    else:
        random_karma = random.randint(1, 7)
    return random_karma


with open('karma.log', 'w', encoding='UTF-8') as file:
    karma = 0
    constant_karma = 500
    while karma < constant_karma:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            file.write(f'{exc}\n')

print('Карма заполнена')
