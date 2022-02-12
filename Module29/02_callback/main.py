
from typing import Callable, Any
app = dict()


def callback(key: Any) -> Callable:
    def rise_func(func: Any) -> Callable:
        app[key] = func()
        return func
    return rise_func


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route
    print('Ответ:', response)
else:
    print('Такого пути нет')

# Пример функции, которая возвращает ответ сервера
# Ответ: OK