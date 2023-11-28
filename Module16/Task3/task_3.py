import datetime
import functools
import time
from typing import Callable, Any

print('Задача 3. Логирование в формате\n')


def log_func(cls, func: Callable, date_format: str) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Запускается {cls.__name__}.{func.__name__}. '
              f'Дата и время запуска {datetime.datetime.now().strftime(date_format)}')
        start_timer = time.time()
        res = func(*args, **kwargs)
        execution_time = round(time.time() - start_timer, 3)
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {execution_time} s')
        return res

    return wrapped_func


def log_methods(date_format: str) -> Callable:
    def decorator(cls) -> Any:
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                method = getattr(cls, i_method)
                decorated_method = log_func(cls, method, date_format)
                setattr(cls, i_method, decorated_method)
        return cls

    return decorator


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
