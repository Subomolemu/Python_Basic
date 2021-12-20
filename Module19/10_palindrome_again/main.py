string = input('Введите строку: ')
count = 0
set_string = set(string)

for sym in set_string:
    if string.count(sym) % 2 != 0:
        count += 1

if count >= 2:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')



