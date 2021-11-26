first_list = []
second_list = []

for i in range(3):
    print('Введите', i + 1, 'число для первого списка: ', end='')
    num = int(input())
    first_list.append(num)

print()

for i in range(7):
    print('Введите', i + 1, 'число для второго списка: ', end='')
    num = int(input())
    second_list.append(num)

first_list.extend(second_list)

for num in first_list:
    while first_list.count(num) > 1:
        first_list.remove(num)

print('Новый первый список с уникальными элементами:', first_list)
