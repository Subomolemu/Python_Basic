class Human:
    satiety = 50
    
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def eat(self):
        print(f'\n---{self.name}---\nИду кушать.')
        self.house.food -= 1
        self.satiety += 1
        print(f'В холодильнике осталось {self.house.food} единиц еды\n'
              f'Сытость поднялась до {self.satiety} единиц')
    
    def work(self):
        print(f'\n---{self.name}---\nИду на работу.')
        self.satiety -= 1
        self.house.money += 1
        print(f'После работы голод опустился до {self.satiety} единиц\n'
              f'Денег стало {self.house.money} единиц')
    
    def play(self):
        self.satiety -= 1
        print(f'\n---{self.name}---\nХочу поиграть.\n сытость снизилась до'
              f' {self.satiety} единиц')
    
    def buy_food(self):
        print(f'\n---{self.name}---\nПора сходить в магазин')
        self.house.food += 1
        self.house.money -= 1
        print(f'После покупки еды ее количество поднялось до {self.house.food}'
              f'единиц.\n'
              f'Но количество денег уменьшилось, осталось {self.house.money} '
              f'единиц денег')
    
    def check_life(self):
        if self.satiety == 0:
            print(f'\n---{self.name}---\nГолод опустился до {self.satiety}. '
                  f'Вы умерли.')
            return False
        