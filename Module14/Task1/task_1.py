import functools
from typing import Callable, Any

print('Задача 1. Как дела?\n')


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        user_condition = input('Введите ваше состояние: ')
        print(f'Как дела? {user_condition}')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def get_square_num(num) -> int:
    return num ** 2


test()

my_num = 2
print(get_square_num(my_num))
