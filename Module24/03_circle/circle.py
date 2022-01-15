import math


class Circle:
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def find_p(self):
        p = 2 * math.pi * self.r
        return p
    
    def find_s(self):
        s = math.pi * self.r ** 2
        return s
    
    def rise(self, k):
        self.r *= k
    
    def find_intersection(self, any_round):
        distance = round(math.sqrt((self.x - any_round.x) ** 2
                                   + (self.y - any_round.y) ** 2), 2)
        print('\nПоиск точек пересечения окружностей...')
        if distance > (self.r + any_round.r) or distance < abs(
                (self.r - any_round.r)):
            print('Окружности не пересекаются.')
        else:
            print('Окружности пересекаются в двух точках. ')
            