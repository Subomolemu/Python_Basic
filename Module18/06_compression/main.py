string = input('Введите строку: ')
code_string = ''
old_sym = string[0]
count = 1
print(code_string)

for i in range(1, len(string)):
    if string[i] == old_sym:
        count += 1
    else:
        code_string += old_sym + str(count)
        count = 1
    old_sym = string[i]

code_string += old_sym + str(count)

print('Закодированная строка', code_string)
