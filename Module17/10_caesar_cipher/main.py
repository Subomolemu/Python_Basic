def check(symbol, alpha, i_shift):
    while alpha.index(symbol) + i_shift > 33:
        index = (alpha.index(symbol) + i_shift) % len(alpha)
        return index
    else:
        index = (alpha.index(symbol) + i_shift)
        return index


text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмyнопрстуфхцчшщъыьэюя'
new_text = [alphabet[check(sym, alphabet, shift)] if sym in alphabet else ' ' for sym in text]
for i_sym in new_text:
    print(i_sym, end='')
