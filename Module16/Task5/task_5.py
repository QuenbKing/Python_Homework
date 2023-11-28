from typing import Callable, Any

print('Задача 5. Синглтон\n')


def singleton(cls: Callable) -> Callable:
    new_cls = None

    def wrapper() -> Any:
        nonlocal new_cls
        if new_cls is None:
            new_cls = cls
        return new_cls

    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
