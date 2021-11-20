films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
like_films = []
in_stock = False

print('Для окончания формирования списка введите: end')
movie_title = input('Введите название любимого фильма: ')

while movie_title != 'end':

    for i in range(9):
        if films[i] == movie_title:
            like_films.append(films[i])
            print('В список добавлен фильм: "' + films[i] + '".\n')
            in_stock = False
            break
        else:
            in_stock = True

    if in_stock:
        print('\nОшибка. Такого фильма нет на сайте.\n')
    in_stock = False

    movie_title = input('Введите название любимого фильма: ')

print('=' * 25, '\nКонец формирования списка.')
print('Список любимых фильмов:', like_films)
