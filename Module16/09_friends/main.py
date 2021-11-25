def balance(friend_one, friend_two, credit):
    friends_list[friend_one - 1][1] += credit
    friends_list[friend_two - 1][1] -= credit


def control(friend_one, friend_two):
    while friend_one == friend_two:
        print('Самому у себя в долг брать нельзя.\n')
        friend_two = int(input('От кого: '))
    return friend_two


friends = int(input('Введите количество друзей: '))
total_credit = int(input('Введите количество расписок: '))
friends_list = []
friend_balance = [0, 0]

for n in range(friends):
    friend_balance[0] = n + 1
    friends_list.append(friend_balance)
    friend_balance = [0, 0]


for count in range(total_credit):
    print()
    print(count + 1, 'расписка')

    to_friend = int(input('Кому: '))
    from_friend = int(input('От кого: '))

    if to_friend == from_friend:
        from_friend = control(to_friend, from_friend)

    how_much_money = int(input('Сколько: '))
    balance(to_friend, from_friend, how_much_money)

print('\nБаланс друзей: ')

for count in range(friends):
    print(friends_list[count][0], ':', friends_list[count][1])
