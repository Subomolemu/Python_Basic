import random


def delete_stick(left_num, right_num):
    for i_stick in range(len(stick_list)):
        if (i_stick >= left_num - 1) and (i_stick < right_num) and (i_stick != '.'):
            stick_list[i_stick] = '.'
    print('Сбиты палки с номера', left, 'по номер', right)
    print(stick_list)


stick = int(input('Введите количество палок: '))
throw = int(input('Введите количество бросков: '))
stick_list = ['|' for _ in range(stick)]
for i in range(throw):
    print('\nБросок', i + 1, end='. ')
    left = random.randint(1, stick)
    right = random.randint(1, stick)
    while left >= right:
        left = random.randint(1, stick)
        right = random.randint(1, stick)
    delete_stick(left, right)

