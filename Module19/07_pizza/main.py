amt_order = int(input('Введите количество заказов: '))
date = {}

for num in range(1, amt_order + 1):
    surname, pizza, total = input(f'{num} заказ: ').split()
    if surname in date.keys() and pizza in date.get(surname, ''):
        date[surname][pizza] += int(total)
    elif surname not in date.keys():
        date[surname] = {pizza: int(total)}
    else:
        date[surname].update({pizza: int(total)})

print()
for i_surname, i_pizza in date.items():
    print(f'{i_surname}:')
    for i in sorted(i_pizza):
        print(f'\t\t{i}: {i_pizza[i]}')
