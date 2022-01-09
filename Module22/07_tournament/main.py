def check_points(string, points):
    string = string.split()
    if int(string[2]) <= points:
        return False
    else:
        return True


min_points = int(input('Введите минимальный порог баллов для прохода во '
                       'второй тур: '))
total_members = int(input('Сколько всего участников: '))

first_tour = open('first_tour.txt', 'w')
first_tour.write(f'{min_points}\n')

for i_member in range(total_members):
    member = input('Введите фамилию, имя, количество баллов через пробел: ')
    first_tour.write(f'{member}\n')

first_tour.close()
first_tour = open('first_tour.txt', 'r')
second_tour = open('second_tour.txt', 'w')
count = 0
second_tour.write('1\n')
# не пойму как вставлять текст без перезаписи
# зарезервировал место под количество участников

for index, i_string in enumerate(first_tour):
    if index == 0:
        continue
    else:
        if check_points(i_string, min_points):
            count += 1
            date_member = i_string.split()
            past_member = f'{count}) {date_member[1][0]}. {date_member[0]} ' \
                          f'{date_member[2]}\n'
            second_tour.write(past_member)

second_tour.seek(0)
second_tour.write(f'{count}\n')
second_tour.close()
