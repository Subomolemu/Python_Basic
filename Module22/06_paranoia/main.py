def cezar(word, alpha, shift):
	b = []
	for sym in word:
		if sym == '\n':
			continue
		if sym.isupper():
			lower_sym = sym.lower()
			index_sym = alpha[(alpha.index(lower_sym) + shift % 26)]
			index_sym = index_sym.upper()
			b.append(index_sym)
		else:
			index_sym = alpha[(alpha.index(sym) + shift) % 26]
			b.append(index_sym)
	b = ''.join(b)
	return b
	
	
alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_str = int(input('Сколько строк в файле: '))
text = open('text.txt', 'w')

for i_str in range(total_str):
	append_word = input(f'Введите {i_str + 1} строку: ')
	text.write(f'{append_word}\n')
	
text.close()

text = open('text.txt', 'r')
cipher_text = open('cipher_text.txt', 'w')

for index, i_str in enumerate(text):
	shift_word = cezar(i_str, alphabet, index + 1)
	cipher_text.write(f'{shift_word}\n')
	
text.close()
cipher_text.close()
