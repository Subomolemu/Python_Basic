def check(symbol, alpha, i_shift):
    while alpha.index(symbol) + i_shift > 25:
        index = (alpha.index(symbol) + i_shift) % len(alpha)
        return index
    else:
        index = (alpha.index(symbol) + i_shift)
        return index


flag = False
finish_text = []
a = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju'.lower()
shift = 25
new_text = [alphabet[check(sym, alphabet, shift)] if sym in alphabet else sym for sym in text]
print(new_text)
text_str = ''.join(new_text)
print(text_str)
text_str = text_str.split()

text_str = [text_str]

for i_text in text_str:

    for lang in range(len(i_text)):
        i = i_text[lang]

        for sym in range(a):
            i = [symbol for symbol in i]
            popped_sym = i.pop()
            i.insert(0, popped_sym)
            i = ''.join(i)

        index_sym = i_text.index(i_text[lang])
        i_text.remove(i_text[lang])
        i_text.insert(index_sym, i)

    for ind in i_text:
        for i in ind:
            if i == '/':
                flag = True
                i_ind = [sym for sym in ind if sym != '/']
                i_ind = ''.join(i_ind)
                finish_text.append(i_ind)
        if flag:
            break
        finish_text.append(ind)
    a += 1

print(finish_text)

print(text_str)