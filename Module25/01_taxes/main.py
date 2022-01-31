class Property:
    
    def __init__(self, worth, money):
        self.money = money
        self.worth = worth
        
    def tax_assessment(self):
        tax = self.worth / 100
        self.money -= tax
        return self.money
    
    def check_money(self):

        self.money -= self.tax_assessment()
        print()
        if self.money >= 0:
            return f'Вам хватило денег на налог, у вас осталось ' \
                   f'{round(self.money, 2)}\n'
        else:
            return (f'Для оплаты налога вам нехватает '
                    f'{round(abs(self.money), 2)}\n')

    def __str__(self):
        return self.check_money()
    

class Apartment(Property):
        
    def tax_assessment(self):
        tax = self.worth / 1000
        return tax
        
    def __str__(self):
        return f'Налог на квартиру составил {self.tax_assessment()}\n' \
               f'{self.check_money()}'
        
        
class Car(Property):
    
    def tax_assessment(self):
        tax = self.worth / 200
        return tax
    
    def __str__(self):
        return f'Налог на машину составил {self.tax_assessment()}\n' \
               f'{self.check_money()}'


class CountryHouse(Property):
    
    def tax_assessment(self):
        tax = self.worth / 500
        return tax
    
    def __str__(self):
        return f'Налог на дачу составил {self.tax_assessment()}\n' \
               f'{self.check_money()}'
    
    
total_money = int(input('Введите количество денег: '))
all_property = Property(worth=100, money=total_money)

app_cost = int(input('Введите стоимость квартиры: '))
app_tax = Apartment(app_cost, all_property.money)
print(app_tax)

car_cost = int(input('Введите стоимость машины: '))
car_tax = Car(car_cost, app_tax.money)
print(car_tax)

ch_cost = int(input('Введите стоимость дачи: '))
ch_tax = CountryHouse(ch_cost, car_tax.money)
print(ch_tax)
