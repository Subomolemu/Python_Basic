from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> [Callable, str]:
    """ Декоратор выполняет логирование функции, если возникла ошибка, запишет
    ее в файл 'function_errors.log' """
    
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(f'Документация: {func.__doc__}')
            print(f'Название функции: {func.__name__}')
            
            res = func(*args, **kwargs)
            return res
        except TypeError:
            date_now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            with open('function_errors.log', 'a+') as error:
                error.write(f'{square_num.__name__}('
                            f'{date_now}'
                            f') - "TypeError"\n')
    
    return wrapped_func


@logging
def square_num(num: int) -> int:
    """Функция для возведения числа в квадрат"""
    
    return num ** 2


number = 's'
square_number = square_num(number)
print(square_number)
