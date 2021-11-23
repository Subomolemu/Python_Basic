total_rollers = int(input('Введите количество коньков: '))
count_people = 0
rollers = []

for i_roll in range(total_rollers):
    print('Размер', i_roll + 1, 'пары: ', end='')
    size = int(input())
    rollers.append(size)
print()

peoples = int(input('Введите количество людей: '))

for people in range(peoples):
    print('Размер ноги', people + 1, 'человека: ', end='')
    leg_size = int(input())
    for size in rollers:
        if size == leg_size:
            count_people += 1
            rollers.remove(size)
            break

print('\nНаибольшее количество людей, который могут взять ролики:', count_people)
