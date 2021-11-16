def control(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    if count == 4:
        return count
    else:
        return 0


def identical_numbers(a, b):
    for year in range(a, b + 1):
        x1 = year % 10
        x2 = year // 10 % 10
        x3 = year // 100 % 10
        x4 = year // 1000 % 10
        if (x1 == x2 and x1 == x3) or (x1 == x3 and x1 == x4) or (x2 == x3 and x2 == x4) or (x1 == x2 and x1 == x4):
            print(year)


f_year = int(input('Введите первый год, состоящий из четырехзначного числа: '))

while control(f_year) != 4:
    print('Ошибка Ввода! Введите год, состоящий из четырехзначного числа.\n')
    f_year = int(input('Введите первый год, состоящий из четырехзначного числа: '))
    control(f_year)

s_year = int(input('Введите второй год, состоящий из четырехзначного числа: '))

while control(s_year) != 4:
    print('Ошибка Ввода! Введите год, состоящий из четырехзначного числа.\n')
    s_year = int(input('Введите второй год, состоящий из четырехзначного числа: '))
    control(s_year)

identical_numbers(f_year, s_year)
