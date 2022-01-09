def def_sort(a):
    return a[1]


alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = input('Введите строку на английском языке: ')

text = open('text.txt', 'w')
text.write(string)
text.close()
dict_letters = []
text = open('text.txt', 'r')
for i_str in text:
    print(f'Содержимое файла "text.txt":\n'
          f'{i_str}')
    dict_letters = [letter for letter in i_str.lower() if letter in alphabet]

text.close()

analysis = open('analysis.txt', 'w')
uniq_letters = set(dict_letters)
list_uniq_letters = []
for letter in uniq_letters:
    frequency = round(1 / len(dict_letters) * dict_letters.count(letter), 3)
    list_uniq_letters.append([letter, frequency])

list_uniq_letters = sorted(list_uniq_letters)
list_uniq_letters.sort(key=def_sort, reverse=True)

analysis = open('analysis.txt', 'w')
for i in list_uniq_letters:
    string = f'{i[0]} {i[1]}\n'
    analysis.write(string)
analysis.close()

analysis = open('analysis.txt', 'r')
print('\nСодержимое файла analysis.txt:')
for i_str in analysis:
    print(i_str, end='')
analysis.close()
