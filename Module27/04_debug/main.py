from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    """Декоратор, который при каждом вызове декорируемой функции выводит
       её имя (вместе со всеми передаваемыми аргументами) и затем какое
       значение она возвращает. И после этого выводится результат её
       выполнения"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        res = func(*args, **kwargs)
        print(f'Вызывается {func.__name__} ', end='(')
        for i in args:
            if kwargs:
                print(f'"{i}"', end=', ')
            else:
                print(f'"{i}"', end='')
                
        for i, key in enumerate(kwargs.keys()):
            if isinstance(kwargs[key], int):
                a = f"{key}={kwargs[key]}"
            else:
                a = f"{key}='{kwargs[key]}'"
                
            if i + 1 < len(kwargs):
                print(f'{a}', end=', ')
            else:
                print(f'{a}', end='')
                
        print(f')\n"{func.__name__}" вернула значение "{res}"')
        print(res)
        print()
        
    return wrapped_func


@debug
def greeting(name: str, age=None) -> str:
    """Функция выводит индивидуальное приветствие.
       Если в функцию кроме имени передается и возраст, выводит информацию и
       о нем"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(
            name=name, age=age)
    elif not age:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
