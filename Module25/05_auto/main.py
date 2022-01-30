import math


class Auto:
    a = 0
    b = 0
    s = 0
    degree = 0
    
    def __init__(self, x, y, new_degree):
        self.x = x
        self.y = y
        self.degree += new_degree
        
    def move(self, s):
        self.degree = self.degree % 360
        if self.degree < 0:
            self.degree += 360
        rad_degree = self.degree / 57.2958
        self.s = s
        x = s * math.sin(rad_degree)
        y = s * math.cos(rad_degree)
        self.x += x
        self.y += y
            
    def to_turn(self, new_degree):
        self.degree += new_degree
        
    def __str__(self):
        return f'- Текущий угол поворота автомобиля: {self.degree} градусов\n' \
               f'- проехал {self.s} километров\n' \
               f'- движение закончено в точке с координатами ' \
               f'({round(self.x, 2)}, {round(self.y, 2)})\n\n'
    
    
class Bus(Auto):
    passengers = 0
    money = 0
    pay_for_km = 10
    
    def __init__(self, x, y, new_degree):
        super().__init__(x, y, new_degree)
        
    def passengers_entered(self, passengers):
        self.passengers += passengers
        print(f'На остановке вошло пассажиров: {passengers}\n')
        
    def passengers_left(self, passengers):
        self.passengers -= passengers
        print(f'На остановке вышло пассажиров: {passengers}\n')
        
    def move(self, s):
        super().move(s)

        self.money += s * self.pay_for_km * self.passengers
        
    def __str__(self):
        return f'- Текущий угол поворота автобуса: {self.degree} градусов\n' \
               f'- проехал {self.s} километров\n' \
               f'- движение закончено в точке с координатами ' \
               f'({round(self.x, 2)}, {round(self.y, 2)})\n' \
               f'- в автобусе {self.passengers} пассажиров\n' \
               f'- текущая выручка: {self.money}\n'
    
    
car = Auto(0, 0, -20)
car.move(10)
print(car)

bus = Bus(0, 0, 110)
bus.passengers_entered(10)
bus.move(10)
print(bus)
bus.passengers_left(3)
bus.to_turn(0)
bus.move(5)
print(bus)
