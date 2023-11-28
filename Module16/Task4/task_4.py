from typing import Callable, Any

print('Задача 4. Весь мир — декоратор…\n')


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        return func

    return wrapped_func


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        return func(*args, **kwargs)

    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
