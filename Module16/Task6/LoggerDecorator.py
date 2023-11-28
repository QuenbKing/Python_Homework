import time
from typing import Callable
import functools


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args} {kwargs}')
        start = time.time()
        res = self.func(*args, **kwargs)
        print(f'Результат: {res}')
        print(f'Время выполнения: {time.time() - start} секунд')
        return res


