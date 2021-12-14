amount_country = int(input('Введите количество стран: '))
country_dict = dict()

for i in range(1, amount_country + 1):
    country_cities = input(f'{i} страна: ').split()
    citi_list = [x for x in country_cities if x != country_cities[0]]
    country_dict[country_cities[0]] = citi_list


for i in range(1, 4):
    citi = input(f'\n{i} город: ')
    check_citi = False

    for x in country_dict.keys():
        if citi in country_dict[x]:
            country = x
            print(f'Город {citi} расположен в стране {country}.')
            check_citi = True
            break
            
    if not check_citi:
        print(f'По городу {citi} данных нет.')
