people = int(input('Количество человек: '))
drop_number = int(input('Какое число в считалке: '))
print('Значит выбывает каждый', drop_number, 'человек.')

people_list = list(range(1, people + 1))
i_number = 0

while len(people_list) > 1:

    print('\nТекущий круг людей: ', people_list)
    print('Начало счета с номера:', people_list[i_number])
    shift = people_list.index(people_list[i_number])
    i_number = drop_number

    if i_number > len(people_list):
        i_number = (i_number + shift - 1) % len(people_list)

    print('Выбывает человек с номером:', people_list[i_number])
    people_list.remove(people_list[i_number])

    if i_number >= len(people_list):
        i_number = 0

print('\nОстался человек под номером:', people_list[0])
