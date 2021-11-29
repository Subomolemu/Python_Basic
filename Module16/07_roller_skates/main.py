total_rollers = int(input('Введите количество коньков: '))
count_people = 0
rollers = []
leg_sizes = []

for i_roll in range(total_rollers):
    print('Размер', i_roll + 1, 'пары: ', end='')
    size = int(input())
    rollers.append(size)
print()

rollers.sort()
print(rollers)

peoples = int(input('Введите количество людей: '))
print()

for people in range(peoples):
    print('Размер ноги', people + 1, 'человека: ', end='')
    leg_size = int(input())
    leg_sizes.append(leg_size)

leg_sizes.sort()

for i_leg_size in leg_sizes:
    for roll in rollers:
        if i_leg_size <= roll:
            rollers.remove(roll)
            break

print('\nНаибольшее количество людей, который могут взять ролики:', total_rollers - len(rollers))
