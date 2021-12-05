text = input('Сообщение: ')
revers_text = []
i_revers = []

for sym in text:
    if sym.isalpha():
        i_revers.append(sym)
    else:
        i_revers.reverse()
        revers_text.append(i_revers)
        revers_text.append(sym)
        i_revers = []

open_revers_text = [i for sym in revers_text for i in sym]
new_text = ''.join(open_revers_text)
print('Новое сообщение:', new_text)
