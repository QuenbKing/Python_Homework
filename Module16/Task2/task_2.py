from typing import Callable, Any

print('Задача 2. Функция обратного вызова\n')

app = dict()


def callback(path: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[path] = func

        def wrapped_func(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapped_func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
