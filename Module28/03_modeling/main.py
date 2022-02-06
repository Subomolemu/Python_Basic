import math
from typing import List, Union


class Square:
    """Базовый класс, описывающий квадрат, который определяется длиной одной
    из его сторон
    длина стороны (side): int"""
    
    def __init__(self, side: int) -> None:
        self.__side = side
    
    @property
    def side(self) -> int:
        """Геттер, возвращает длину стороны квадрата."""
        return self.__side
    
    @side.setter
    def side(self, side: int) -> None:
        """Сеттер, пропускает длину стороны квадрата, если ее значение больше 0,
        иначе выбрасывает исключение"""
        if side <= 0:
            raise Exception('Длина стороны не может быть равна 0 или '
                            'отрицательному числу')
        else:
            self.__side = side
        
    def area(self) -> int:
        """Метод для определения площади квадрата"""
        return self.__side ** 2
    
    def perimeter(self) -> int:
        """Метод для определения периметра квадрата"""
        return self.__side * 4
    
    
class Triangle:
    """Базовый класс, описывающий треугольник, который определяется длиной
    основания и высотой"""
    def __init__(self, base_length, height) -> None:
        self.__base_length = base_length
        self.__height = height
        
    @property
    def base_length(self) -> int:
        """Геттер, возвращающий длину основания треугольника"""
        return self.__base_length
    
    @base_length.setter
    def base_length(self, base_length) -> None:
        """Сеттер, определяющий длину основания треугольника больше 0,
        иначе вызывает исключение"""
        if base_length <= 0:
            raise Exception('Длина основания не может быть равна 0 или '
                            'отрицательному числу')
        else:
            self.__base_length = base_length

    @property
    def height(self) -> int:
        """Геттер, возвращающий длину высоты треугольника"""
        return self.__height

    @height.setter
    def height(self, height) -> None:
        """Сеттер, определяющий длину высоты треугольника больше 0,
        иначе вызывает исключение"""
        if height <= 0:
            raise Exception('Длина высоты не может быть равна 0 или '
                            'отрицательному числу')
        else:
            self.__height = height
            
    def area(self) -> int:
        """Метод, возвращающий площадь треугольника"""
        return (self.__base_length * self.__height) / 2
    
    def perimeter(self) -> int:
        """Метод, возвращающий периметр треугольника"""
        per = self.__base_length + 2 * math.sqrt(((self.__base_length / 2) **
                                                  2) + self.__height ** 2)
        return per
    

class PerAreaMixin:
    """Миксин, позволяющий посчитать площадь и периметр 3д фигур
    Пирамида и Куб"""
    @classmethod
    def area(cls, figure_list) -> Union[int, float]:
        """Метод, определяющий площадь 3д фигуры"""
        a = 0
        for figure in figure_list:
            a += figure.area()
        
        return a

    @classmethod
    def perimeter(cls, figure_list: List) -> Union[int, float]:
        """Метод, определяющий периметр 3д фигуры"""
        per = 0
        for figure in figure_list:
            per += figure.perimeter()
        return per


class Cube(PerAreaMixin, Square):
    """Дочерний класс, описывающий куб, умеющий определять его площадь и
    периметр через миксин"""
    def __init__(self, side: int) -> None:
        super().__init__(side)
        self.cube_parts = [Square(self.side), Square(self.side),
                           Square(self.side), Square(self.side),
                           Square(self.side), Square(self.side)]
    

class Pyramid(PerAreaMixin, Square, Triangle):
    """Дочерний класс, описывающий пирамиду, умеющий определять его площадь и
        периметр через миксин, в пирамиде сторона квадрата и основание
        треугольника равны"""
    def __init__(self, side: int, height: int) -> None:
        super().__init__(side)
        self.__base_length = side
        self.height = height
        self.pyramid_parts = [Square(self.side), Triangle(self.side, height),
                              Triangle(self.side, height),
                              Triangle(self.side, height),
                              Triangle(self.side, height)]

    
cube = Cube(10)
print(cube.area(cube.cube_parts))
print(cube.perimeter(cube.cube_parts))
pyramid = Pyramid(10, 12)
print(pyramid.area(pyramid.pyramid_parts))
print(pyramid.perimeter(pyramid.pyramid_parts))
