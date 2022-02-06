import math
from typing import Union


class MyMath:
    """Класс для вычисления
    Длины окружности (circle_len)
    Площади окружности (circle_sq)
    Объём куба (cube_volume)
    Площадь поверхности сферы(sphere_area)
    """
    
    @classmethod
    def circle_len(cls, radius: Union[float, int]) -> float:
        return 2 * math.pi * radius
    
    @classmethod
    def circle_sq(cls, radius: Union[float, int]) -> float:
        return math.pi * radius ** 2
    
    @classmethod
    def cube_volume(cls, side: Union[float, int]) -> Union[float, int]:
        return side ** 3
    
    @classmethod
    def sphere_area(cls, radius: Union[float, int]) -> float:
        return 4 * math.pi * radius ** 2
    