import random
import house
import human


def human_logic(hum):
    check = random.randint(1, 6)
    if hum.satiety < 20:
        hum.eat()
    elif hum.house.food < 10:
        hum.buy_food()
    elif hum.house.money < 50:
        hum.work()
    elif check == 1:
        hum.work()
    elif check == 2:
        hum.eat()
    else:
        hum.play()


def input_info(hum):
    print(f'\nИнформация о жителях дома:\n'
          f'\t-Меня зовут {hum.name}\n'
          f'\t-Моя сытость находится на уровне {hum.satiety} единиц\n'
          f'\t-В тумбочке находится {hum.house.money} единиц денег\n'
          f'\t-В холодильнике находится {hum.house.food} единиц еды\n'
          f'\t-Меня можно поздравить, ведь я выжил(а) при таких условиях '
          f'проживания!')


my_house = house.House
human_1 = human.Human('Sergey', my_house)
human_2 = human.Human('Elena', my_house)
day = 0

while day != 365:
    day += 1
    print(f'\nНачался {day} день.')
    human_logic(human_1)
    human_logic(human_2)
    if human_1.check_life() or human_2.check_life():
        break
        
if day == 365:
    input_info(human_1)
    input_info(human_2)
