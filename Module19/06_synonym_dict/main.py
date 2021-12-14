amount_synonyms = int(input('Введите количество пар слов: '))
synonyms_dict = {}
for i in range(1, amount_synonyms + 1):
    synonyms = input(f'{i} пара: ').split(' - ')
    for word in synonyms:
        word.strip()

    synonyms_dict[synonyms[0]] = synonyms[1]

print()
check_word = input('Введите слово: ').lower().title()
flag = True
while True:
    for key, values in synonyms_dict.items():
        if check_word == values:
            print(f'Синоним: {key}')
            flag = False
            break
        elif check_word == key:
            print(f'Синоним: {values}')
            flag = False
            break
    if flag:
        print('Такого слова в словаре нет.')
        check_word = input('Введите слово: ').lower().title()
    else:
        break
