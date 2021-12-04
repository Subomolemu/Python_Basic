# дом машина лес он
text = input('Введите текст через пробелы: ').split()
total_len = 0
total_word = ''

for word in text:
    len_str = len(word)
    if len_str > total_len:
        total_len = len_str
        total_word = word

print('\nСамое длинное слово: {},\nЕго длина: {}'.format(
    total_word,
    total_len
))
