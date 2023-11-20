import functools
from typing import Dict, Any, Callable

print('Задача 5. Кэширование для ускорения вычислений\n')


def hashed(func: Callable) -> Callable:
    hash_dict: Dict[Any, Any] = dict()

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        key = ("{func_name}{func_args}{func_kwargs}"
               .format(func_name=func.__name__, func_args=args, func_kwargs=kwargs))
        if key not in hash_dict:
            hash_dict[key] = func(*args, **kwargs)
        return hash_dict[key]

    return wrapped_func


@hashed
def fibonacci(num: int) -> int:
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


@hashed
def summ(a: int, b: int, c: int) -> int:
    return a + b + c


print(fibonacci(2))
print(fibonacci(2))

print(summ(1, 2, 3))
print(summ(1, 2, 3))

print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(6))
