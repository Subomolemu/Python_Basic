def find_key(struct, cnt, key, lvl_key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        cnt += 1
        if cnt == lvl_key:
            return None
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, cnt, key, lvl_key)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

count = 0
user_key = input('Введите искомый ключ: ')
ask_lvl = input('Хотите ввести максимальную глубину? Y/N: ').strip().lower()
lvl = None
if ask_lvl == 'y':
    lvl = int(input('Введите максимальную глубину: '))
value = find_key(site, count, user_key, lvl)
print(f'\nЗначение ключа: {value}')
