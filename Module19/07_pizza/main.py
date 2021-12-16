amt_order = int(input('Введите количество заказов: '))
date = {}

for num in range(1, amt_order + 1):
    order = input(f'{num} заказ: ').split()

    if order[0] in date.keys() and order[1] in date.get(order[0], ''):
        date[order[0]][order[1]] += int(order[2])
    elif order[0] not in date.keys():
        date[order[0]] = {order[1]: int(order[2])}
    else:
        date[order[0]].update({order[1]: int(order[2])})

print()
for key, value in date.items():
    print(f'{key}:')
    for i in sorted(value):
        print(f'\t\t{i}: {value[i]}')
