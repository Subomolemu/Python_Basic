import random
import warrior


dice_roll = {}
tank = warrior.Warrior('TANK', 300)
dd = warrior.Warrior('DD', 200)
lap = 0

while True:
    lap += 1
    dice_roll[tank.name] = random.randint(1, 10)
    dice_roll[dd.name] = random.randint(1, 10)
    
    if dice_roll[tank.name] > dice_roll[dd.name]:
        damage_generation = random.randint(20, 35)
        dd.get_punch(damage_generation)
        
        print(f'\n{lap} раунд!\n\t{tank.name} нанес противнику '
              f'{damage_generation} урона.\n\tУ {dd.name} осталось: '
              f'{dd.health} хп')
    
    elif dice_roll[tank.name] <= dice_roll[dd.name]:
        damage_generation = random.randint(35, 50)
        tank.get_punch(damage_generation)
        
        print(f'\n{lap} раунд!\n\t{dd.name} нанес противнику '
              f'{damage_generation} урона.\n\tУ {tank.name} осталось '
              f'{tank.health} хп')
    
    if tank.health == 0:
        print(f'\nВ этом бою победил {dd.name}! Осталось хп: {dd.health}')
        break
    
    elif dd.health == 0:
        print(f'\nВ этом бою победил {tank.name}! Осталось хп: {tank.health}')
        break
