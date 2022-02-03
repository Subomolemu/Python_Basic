from typing import Callable
import time


def slowdown(func: Callable) -> Callable:
    time.sleep(2)
    return func


@slowdown
def say_hello(name: str) -> str:
    return f'Hallo, {name}'


my_name = 'Sergey'
func_hello = say_hello(my_name)
print(func_hello)
