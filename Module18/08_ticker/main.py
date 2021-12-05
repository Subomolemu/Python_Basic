f_txt = input('Первая строка: ')
s_txt = input('Вторая строка: ')
chek = False

if f_txt == s_txt:
    print('Первая строка равна второй строке, сдвиг не требуется.')
    chek = True
elif len(s_txt) != len(f_txt):
    print('Ошибка ввода, строки должны быть одинаковой длины.')
else:
    for i in range(len(f_txt)):
        f_txt = [sym for sym in f_txt]
        popped_sym = f_txt.pop()
        f_txt.insert(0, popped_sym)
        f_txt = ''.join(f_txt)
        if f_txt == s_txt:
            print('Первая строка получается из второй со сдвигом', i + 1)
            chek = True
            break
if not chek:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
