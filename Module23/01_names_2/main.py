total_names = int(input('Введите количество имен пользователей: '))
total_count = 0
count = 0
line_count = 0


with open('people.txt', 'w+') as people:
    for i_name in range(total_names):
        name = input('Введите имя, в котором символов не меньше трех: ')
        people.write(f'{name}\n')
    people.seek(0)

    with open('errors.log', 'w', encoding='utf-8') as errors:
        for i_name in people:
            line_count += 1
            try:
                for sym in i_name:
                    count += 1
                    if sym == '\n':
                        count -= 1
                if count < 3:
                    total_count += count
                    count = 0
                    raise ValueError(f'В имени {i_name} '
                                     f'меньше трех символов.')
                    
                total_count += count
                count = 0

            except ValueError:
                redact_names = [sym for sym in i_name if sym != '\n']
                redact_names = ''.join(redact_names)
                error = f'{redact_names} - в этом имени меньше трех символов.' \
                        f' Строка возникновения ошибки номер {line_count}\n'
                errors.write(error)
                
print(f'\nОбщая сумма символов равна {total_count}')
