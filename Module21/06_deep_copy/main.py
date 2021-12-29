def find_key(struct, tab, cnt, mod):

    for key, value in struct.items():
        if cnt != 2:
            print(f"{tab}'{key}': ""{")
        else:
            a = value.split()

            if 'телефон' in a:
                a[a.index('телефон')] = mod
            a = ' '.join(a)
            print(f"{tab}'{key}': '{a}'.")

        if isinstance(value, dict):
            find_key(value, tab * 2, cnt + 1, mod)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


total_site = int(input('Сколько сайтов: '))
list_mod = []
count = 0
t = '\t'

for _ in range(total_site):
    model = input('Введите название продукта для нового сайта: ')
    list_mod.append(model)

    for i_model in list_mod:
        print(f'Сайт для {i_model}')
        print('site = {')
        find_key(site, t, count, i_model)

        for num in range(2, -1, -1):
            if num != 0:
                print(t * num + '}')
            else:
                print('}')
    print()
