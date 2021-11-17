def coin_search():
    if (x ** 2 + y ** 2) ** 0.5 <= r:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')


print('Введите координаты понетки: ')
x = float(input('X = '))
y = float(input('Y = '))
r = float(input('Введите радиус: '))
coin_search()
