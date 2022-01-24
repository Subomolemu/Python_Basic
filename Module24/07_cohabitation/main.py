import human
import house


my_house = house.House(50, 0)
human_1 = human.Human('Sergey', my_house)
human_2 = human.Human('Elena', my_house)

humans = [human_1, human_2]

for day in range(365):
    for human in humans:
        print(f'\nНачался {day + 1} день.')
        human.act()
        if human_1.check_life() or human_2.check_life():
            break
            
for human in humans:
    human.input_info()
