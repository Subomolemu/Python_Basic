from typing import Callable, Any


def rise_question(func: Callable) -> Callable:
    """ Декоратор для вывода вопроса "как дела?" """
    
    def wrapped_func(*args, **kwargs) -> Any:
        answer = input('Как дела?\n- ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        res = func(*args, **kwargs)
        return res
    return wrapped_func
    
    
@rise_question
def sum_square(number: int) -> int:
    summa = 0
    for i in range(1, number + 1):
        summa += i ** 2
    return summa


@rise_question
def say_hello(name: str) -> str:
    return f'Hallo, {name}'


my_name = 'Sergey'
num = 10
my_func = sum_square(num)
print(my_func)
print()
func_hello = say_hello(my_name)
print(func_hello)
