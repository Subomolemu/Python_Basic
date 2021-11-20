word = input('Введите слово: ')
symbols = []
count_sym = 0
count = 1

for symbol in word:
    symbols.append(symbol)

for i in range(len(symbols)):

    for sym in symbols:
        if symbols[i] != sym:
            count += 1

    if count == len(symbols):
        count_sym += 1
    count = 1

print('Колличество уникальных букв:', count_sym)
