import functools
from typing import Callable, Any


def callback(key: Any) -> Callable:
    def rise_func(func: Any) -> Callable:
        
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> str:
            res = func(*args, **kwargs)
            app[key] = res
            return res
        return wrapped
    return rise_func


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {}
example()
route = app.get('//')
if route:
    response = route
    print('Ответ:', response)
else:
    print('Такого пути нет')

# Пример функции, которая возвращает ответ сервера
# Ответ: OK