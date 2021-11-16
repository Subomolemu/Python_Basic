def coin_search():
    if x * 2 <= r and y * 2 <= r:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')


print('Введите координаты понетки: ')
x = float(input('X = '))
y = float(input('Y = '))
r = int(input('Введите радиус: '))
coin_search()
