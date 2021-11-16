def min_div(num):
    while num < 1:
        print('Ошибка ввода.')
        num = int(input('Введите число n > 0: '))

    for divider in range(2, num + 1):
        if num % divider == 0:
            print('Наименьший делитель, отличный от едиицы:', divider)
            break


number = int(input('Введите число n > 0: '))

min_div(number)
