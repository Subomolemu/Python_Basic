def revers_number(number):
    int_revers_num = ''
    div_revers_num = '0.'
    number = str(number)

    for symbol in number:
        if symbol != '.':
            int_revers_num = symbol + int_revers_num
        else:
            break

    for symbol in number[::-1]:
        if symbol != '.':
            div_revers_num += symbol
        else:
            break

    revers_num = int(int_revers_num) + float(div_revers_num)
    return revers_num


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

print()
print('Первое число наборот::', revers_number(first_number))
print('Второе число наборот:', revers_number(second_number))
print('Сумма этих чисел:', revers_number(first_number) + revers_number(second_number))
