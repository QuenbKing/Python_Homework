import functools
from typing import Callable, Any, Dict

print('Задача 4. Счётчик\n')

FUNCTIONS_CALLS: Dict[Callable, int] = dict()


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        if func.__name__ in FUNCTIONS_CALLS:
            FUNCTIONS_CALLS[func.__name__] += 1
        else:
            FUNCTIONS_CALLS[func.__name__] = 1
        return func(*args, **kwargs)

    return wrapped_func


@counter
def say_hello(name: str) -> str:
    return f'Hello {name}!'


@counter
def say_goodbye(name: str) -> str:
    return f'Goodbye {name}!'


print(say_hello('Tom'))
print(say_hello('John'))
print(FUNCTIONS_CALLS)

print(say_goodbye('Tom'))
print(FUNCTIONS_CALLS)
