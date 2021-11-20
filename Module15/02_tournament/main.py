sportsman_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
count = 0
first_day_list = []

for name in sportsman_list:
    if count % 2 == 0:
        first_day_list.append(name)
    count += 1

print('Список участников турнира на первый день:', )
print(first_day_list)
