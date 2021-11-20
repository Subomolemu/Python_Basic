word = input('Введите слово: ')
symbols = []
flag = False

revers_symbols = []

for symbol in word:
    symbols.append(symbol)


for i in range(-1, -len(symbols) - 1, -1):
    revers_symbols.append(symbols[i])
    if symbols[-len(symbols) - i - 1] != revers_symbols[-i - 1]:
        print('\nСлово не является палиндромом.')
        break
    else:
        flag = True

if flag:
    print('\nСлово является палиндромом.')
