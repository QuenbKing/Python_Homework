from collections.abc import Callable
from typing import Any

print('Задача 1. Права доступа\n')

user_permissions = ['admin']


def check_permission(permission: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs) -> Any:
            if permission in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError(f'у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapped_func

    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as exc:
    print(f'{exc.__class__.__name__}: {exc}')
