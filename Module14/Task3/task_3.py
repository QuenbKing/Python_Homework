import datetime
import functools
from typing import Callable, Any

print('Задача 3. Логирование\n')


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'{func.__name__}: {func.__doc__}', end='.\n')
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='UTF-8') as file:
                file.write(f'{datetime.datetime.now()}: {func.__name__} ({exc})\n')

    return wrapped_func


@logging
def summ_three_nums(a: int, b: int, c: int) -> int:
    """Функция, которая суммирует три аргумента типа int"""
    return a + b + c


@logging
def get_exception() -> None:
    """Функция, которая выдаёт ошибку"""
    raise Exception('Где-то произошла ошибка')


print(summ_three_nums(1, 2, 3))
get_exception()
get_exception()
