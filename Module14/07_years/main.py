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
        for num in str(year):
            if str(year).count(num) >= 3:
                print(year)
                break


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
