def came(name):
    if len(guests) >= 6:
        print('Прости,', name + ', мест больше нет.')
    else:
        print('Привет,', name + '!')
        guests.append(name)
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)


def gone(name):
    print('Пока,', name + '!')
    guests.remove(name)
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
end = 'пора спать'

print('Сейчас на вечеринке', len(guests), 'человек:', guests)
print('Гость пришел или ушел? - ', end='')
ask = input()


while ask != end:
    name_guest = input('Имя гостя: ')

    if ask == 'пришел':
        came(name_guest)
    elif ask == 'ушел':
        gone(name_guest)
    print('Гость пришел или ушел? - ', end='')
    ask = input()

    if ask == end:
        print('\nВечеринка закончилась, все легли спать.')
        break
