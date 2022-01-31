class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    
class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def profit(self):
        return 0
    

class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__money = 13000
        
    def profit(self):
        return self.__money
    
    def __str__(self):
        return 'Менеджер'
    
    
class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales
        self.__money = 5000
        
    def profit(self):
        return self.__money + (self.__sales * 5 / 100)

    def __str__(self):
        return 'Агент'
    

class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours
        self.__money = 100
    
    def profit(self):
        return self.__money * self.__hours
    
    def __str__(self):
        return 'Рабочий'
    
    
emp_list = []
sergey = Manager(name='Sergey', surname='Sergeev', age=27)
andrey = Manager(name='Andrey', surname='Andreev', age=25)
vladimir = Manager(name='Vladimir', surname='Vladimirov', age=23)
kirill = Agent(name='Kirill', surname='Kirillov', age=22, sales=20000)
anton = Agent(name='Anton', surname='Antonov', age=21, sales=15000)
vlad = Agent(name='Vlad', surname='Vladov', age=24, sales=30000)
jon = Worker(name='Jon', surname='Jonov', age=24, hours=20)
ken = Worker(name='Ken', surname='Kenov', age=24, hours=15)
dima = Worker(name='Dima', surname='Dimov', age=24, hours=25)
emp_list.append(sergey)
emp_list.append(andrey)
emp_list.append(vladimir)
emp_list.append(kirill)
emp_list.append(anton)
emp_list.append(vlad)
emp_list.append(jon)
emp_list.append(ken)
emp_list.append(dima)

for i, emp in enumerate(emp_list):
    print(f'-----------------------\n'
          f'{i + 1}) {emp.get_name()} {emp.get_surname()}\n'
          f'Возраст {emp.get_age()} лет.\n'
          f'Должность {emp}\n'
          f'Ежемесячная зарплата {emp.profit()} рублей.')
    