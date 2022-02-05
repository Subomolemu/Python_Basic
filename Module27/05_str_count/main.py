from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {wrapper.count} раз')
        return res

    wrapper.count = 0
    return wrapper


@counter
def test():
    print('test')
    
    
test()
test()
test()