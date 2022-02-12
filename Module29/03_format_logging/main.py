import functools
from datetime import datetime
import time
from typing import Callable, Any


def timer(func: Callable, cls_name: str, format_date: str) -> Any:
    """
    Декоратор функций в классах.
    Используется для вывода даты запуска функции, и времени ее работы.
    Ее аргументы:
    - func: принимает функцию, которую декорирует
    - cls_name: получает название класса из того класса, метод которого
                декорируется для его отображение при выводе информации.
    - format_date: получет строку, к примеру: "b d Y - H:M:S", форматирует
                   ее для корректного использования в аргументах метода
                   ".strftime()"
    Возвращает декорированную функцию
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Callable:
        
        print(f'Запуск "{cls_name}.{func.__name__}". Дата и время запуска: '
              f'{datetime.utcnow().strftime(format_date)}')
        
        start = time.time()
        res = func(*args, **kwargs)
        
        print(f'Завершение "{cls_name}.{func.__name__}", время работы  '
              f'{round(time.time() - start, 3)}s')
        return res
    return wrapped


def log_methods(date: str) -> Callable:
    """
    Декоратор класса, использует декоратор функцию @timer ко всем методам
    класса, в качестве аргумета принимает строку: "b d Y - H:M:S", форматирует
    ее для корректного использования в аргументах метода ".strftime()".
    Возвращает класс с декорированными методами.
    """
    date = [i if not i.isalpha() else f'%{i}' for i in date]
    date = ''.join(date)
    
    def all_methods(cls: Callable) -> Callable:
        for method in dir(cls):
            if method.startswith("__") is False:
                cur_method = getattr(cls, method)
                decor_method = timer(func=cur_method,
                                     cls_name=f'{cls.__name__}',
                                     format_date=date)
                setattr(cls, method, decor_method)
        return cls
    return all_methods


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print('наследник тест сум')
    
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
# - Завершение 'B.test_sum_2', время работы = 0.370s
