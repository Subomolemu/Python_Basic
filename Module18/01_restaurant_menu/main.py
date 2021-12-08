menu_from_the_site = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню:', menu_from_the_site, '\n')
menu = ', '.join(menu_from_the_site.split(';')).title()
print('На данный момент в меню есть:\n' + menu)
