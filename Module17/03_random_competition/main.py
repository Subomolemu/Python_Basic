import random

list_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
list_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда:', list_1)
print('Вторая команда:', list_2)
total_list = [list_1[x] if list_1[x] >= list_2[x] else list_2[x] for x in range(20)]
print('Победители тура:', total_list)
