import functools
import time
from typing import Callable, Any

print('Задача 2. Замедление кода\n')


def program_fell_sleep(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        seconds_count = 5
        print(f'Подождите {seconds_count} секунд')
        for second in range(1, seconds_count + 1):
            time.sleep(1)
            print(f'{second}...')
        print('Ответ получен')
        return func(*args, **kwargs)

    return wrapped_func


@program_fell_sleep
def get_square_num(num: int) -> int:
    return num ** 2


@program_fell_sleep
def factorial(num: int) -> int:
    res = 1
    for i_num in range(num, 1, -1):
        res *= i_num
    return res


print(get_square_num(2))
print(factorial(5))
