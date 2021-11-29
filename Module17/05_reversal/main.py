text = input('Введите строку, в котором символ "h" встречается минимум 2 раза: ')
min_h = text.index('h')
max_h = text.index('h', -1)
print(text[max_h - 1:min_h:-1])
