string = input('Введите строку: ')
last_sym = ''

for i in range(len(string)):
    if string[i] != last_sym:
        print(string[i]+str(string.count(string[i])), end='')
        last_sym = string[i]
