import random


class Family:
    satiety = 30
    happy = 100
    
    def __init__(self, name, home):
        self.name = name
        self.home = home
    
    def eating(self):
        print(f'{self.name} кушает')
        for _ in range(30):
            if self.home.food == 0:
                print('Еда в холодильнике закончилась. Надо Идти в магазин.')
                break
            self.satiety += 1
            self.home.food -= 1
            self.home.total_food += 1
    
    def play_for_cat(self):
        self.happy += 5
        self.satiety -= 10
        print('Игры с котом...')
    
    def check_status(self):
        if self.satiety <= 0:
            print(f'К сожалению, {self.name} умер(умерла) от голода.')
            return False
        if self.happy < 10:
            print(f'К сожалению {self.name} умер(умерла) от депрессии')
            return False
        return True
    
    def __str__(self):
        return f'---{self.name}---\n' \
               f'\t-Уровень сытости - {self.satiety} единиц\n' \
               f'\t-Уровень счастья - {self.happy} единиц'
    

class Man(Family):
    def __init__(self, name, home):
        super().__init__(name, home)
    
    def work(self):
        self.home.money += 150
        self.satiety -= 10
        self.home.total_money += 150
        print(f'{self.name} идет на работу.')
    
    def play_pc(self):
        self.happy += 20
        self.satiety -= 10
        print('Надо поиграть в компьютер.')
    
    def actions(self):
        check = random.randint(1, 10)
        if self.satiety <= 20 and self.home.food > 0:
            self.eating()
        elif self.happy <= 100:
            self.play_pc()
        elif self.home.money <= 50:
            self.work()
        elif check == 1:
            self.play_for_cat()
        self.check_status()


class Woman(Family):
    def __init__(self, name, home):
        super().__init__(name, home)
    
    def pay_food(self):
        while self.home.food <= 50:
            self.home.food += 10
            self.home.money -= 10
        while self.home.food_for_cat <= 10:
            self.home.food_for_cat += 10
            self.home.money -= 10
        self.satiety -= 10
        print(f'{self.name} идет за едой для семьи в магазин.')
    
    def pay_coat(self):
        self.happy += 60
        self.home.money -= 350
        self.home.total_coat += 1
        print('Нет настроения, надо срочно купить шубу.')
    
    def clean_home(self):
        self.home.dirt -= 100
        self.satiety -= 10
        if self.home.dirt < 0:
            self.home.dirt = 0
        print('В доме очень грязно, время уборки.')
    
    def actions(self):
        check = random.randint(1, 10)
        if self.satiety <= 20 and self.home.food > 0:
            self.eating()
        elif self.happy <= 100:
            self.pay_coat()
        elif self.home.food <= 20 or self.home.food_for_cat <= 10:
            self.pay_food()
        elif self.home.dirt >= 110:
            self.clean_home()
        elif check == 1:
            self.play_for_cat()
        self.check_status()


class Baby(Family):
    def __init__(self, name, home):
        super().__init__(name, home)
    
    def play(self):
        self.happy += 10
        print(f'Ребенок {self.name} играет')
        self.home.dirt += 10
    
    def eating(self):
        print(f'Ребенок {self.name} кушает')
        for _ in range(20):
            if self.home.food == 0:
                print('Еда в холодильнике закончилась. Надо Идти в магазин.')
                break
            self.satiety += 1
            self.home.food -= 1
            self.home.total_food += 1
        self.home.dirt += 10
    
    def sleep(self):
        self.satiety -= 10
    
    def actions(self):
        check = random.randint(1, 10)
        if self.satiety <= 20 and self.home.food > 0:
            self.eating()
        elif self.happy < 100:
            self.play()
        elif check == 1:
            self.play_for_cat()
        elif check == 2:
            self.sleep()
        self.check_status()
    
    def __str__(self):
        return f'---Ребенок {self.name}---\n' \
               f'\t-Уровень сытости - {self.satiety} единиц\n' \
               f'\t-Уровень счастья - {self.happy} единиц'


class Cat(Family):
    def __init__(self, name, home):
        super().__init__(name, home)
    
    def eating(self):
        for _ in range(10):
            if self.home.food_for_cat == 0:
                print('Еда в холодильнике закончилась. Надо Идти в магазин.')
                break
            self.satiety += 2
            self.home.food_for_cat -= 1
            self.home.total_food += 1
        print(f'Кот {self.name} покушал.')
    
    def sleep(self):
        self.satiety -= 10
        print(f'Кот {self.name} спит.')
    
    def tear_wallpaper(self):
        self.home.dirt += 5
        self.satiety -= 10
        print(f'Кот {self.name} портит обои.')
    
    def actions(self):
        check = random.randint(1, 2)
        if self.satiety <= 20 and self.home.food > 0:
            self.eating()
        elif check == 1:
            self.sleep()
        elif check == 2:
            self.tear_wallpaper()
        self.check_status()
    
    def __str__(self):
        return f'---Кот {self.name}---\n' \
               f'\t-Уровень сытости - {self.satiety} единиц'


class Home:
    money = 100
    food = 50
    food_for_cat = 30
    dirt = 0
    total_coat = 0
    total_money = 0
    total_food = 0
    
    def __init__(self):
        pass
    
    def home_pollution(self):
        self.dirt += 5
        print('Под конец дня в доме стало немного грязнее...')
    
    def __str__(self):
        return f'\nСправка по дому:\n' \
               f'\t- В тумбочке осталось {self.money} денег.\n' \
               f'\t- В холодильнике осталось {self.food} еды.\n' \
               f'\t- У Кота осталось {self.food_for_cat} еды.\n' \
               f'\t- Уровень грязи - {self.dirt} единиц.'
    
    def all_for_year(self):
        print(f'\nЗа год:\n '
              f'\t- съели {self.total_food} еды.\n'
              f'\t- Заработали {self.total_money} денег.\n'
              f'\t- Куплено {self.total_coat} шуб.')


my_home = Home()
man = Man('Сергей', my_home)
woman = Woman('Елена', my_home)
baby = Baby('Ева', my_home)
cat_1 = Cat('Васька', my_home)
cat_2 = Cat('Петька', my_home)
family_list = [man, woman, baby, cat_1, cat_2]
status = True

for i in range(365):
    print(f'\n{i + 1} день жизни.\n')
    
    for resident in family_list:
        print(resident)
        resident.actions()
        status = resident.check_status()
        print()
        if not status:
            break
    
    my_home.home_pollution()
    print(my_home)
    if not status:
        print('Не удалось прожить год')
        break
    if i + 1 == 365:
        my_home.all_for_year()
