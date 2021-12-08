def check(symbol, alpha, i_shift):
    while alpha.index(symbol) + i_shift > 25:
        index_sym = (alpha.index(symbol) + i_shift) % len(alpha)
        return index_sym
    else:
        index_sym = (alpha.index(symbol) + i_shift)
        return index_sym


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ' \
       'ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt ' \
       'uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu ' \
       't/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdj' \
       'umzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip ' \
       'fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf w' \
       'jpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu ' \
       'cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg ' \
       'fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ' \
       'ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.lower()

shift = 25
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_text = [alphabet[check(sym, alphabet, shift)] if sym in alphabet else sym for sym in text]

for index, symbol in enumerate(new_text):
    if symbol == '(':
        new_text[index] = "'"
    elif symbol == '+':
        new_text[index] = '"'

new_text = ''.join(new_text).split()
text = []


x = 3  # сдвиг символов в строке
a = [sym for sym in new_text[0]]  # рабочая строка для реализации сдвига строки в списке

for i in range(1, len(new_text)):
    index = new_text[i]

    for _ in range(x):
        popped_sym = a.pop()
        a.insert(0, popped_sym)

    a = ''.join(a)
    new_text.pop(i - 1)
    new_text.insert(i - 1, a)

    a = [sym for sym in new_text[i]]
    if '/' in a:
        x += 1

print('Дзен питона:\n-', end=' ')
for i in new_text:
    if '/' not in i:
        print(i, end=' ')
    else:
        no_slash_i = [sym for sym in i if sym != '/']
        no_slash_i = ''.join(no_slash_i)
        print(no_slash_i)
        print('-', end=' ')
