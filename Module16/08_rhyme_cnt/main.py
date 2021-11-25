people = int(input('Количество человек: '))
drop_number = int(input('Какое число в считалке: '))
print('Значит выбывает каждый 7 человек.')

people_list = list(range(1, people + 1))
i_number = people_list[0]
transfer_list = list(range(1, people + 1))

while len(people_list) > 1:

    print('\nТекущий круг людей: ', transfer_list)
    print('Начало счета с номера:', people_list[0])
    i_number = drop_number

    if i_number > len(people_list):
        i_number %= len(people_list)

    print('Выбывает человек с номером:', people_list[i_number - 1])
    transfer_list.remove(people_list[i_number - 1])
    people_list.remove(people_list[i_number - 1])
    countdown = people_list[i_number - 1]

    while people_list[0] != countdown:
        num_transfer = people_list[0]
        people_list.remove(people_list[0])
        people_list.append(num_transfer)

print('\nОстался человек под номером:', people_list[0])
