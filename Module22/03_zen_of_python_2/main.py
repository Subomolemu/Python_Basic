import os


def check(check_word):
    if not check_word:
        return 0
    
    for sym in check_word:
        if sym.isalpha():
            continue
        else:
            check_word = [symbol for symbol in check_word]
            check_word.remove(sym)

            check_word = ''.join(check_word)
            
        if check_word.isalpha():
            return 1
        else:
            return check(check_word)
        

count_letter = 0
count_word = 0
count_string = 0
text = []

way_to_zen = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
zen = open(way_to_zen, 'r')

for i in zen:
    count_string += 1
    string = i.split()
    text.append(i)
    
    for word in string:
        
        if word.isalpha():
            count_word += 1
        else:
            count_word += check(word)
            
    for letter in i:
        if letter.isalpha():
            count_letter += 1
    
zen.close()
text = ''.join(text).lower()
letters = set(text)

min_i = ''
min_count_letter = count_letter

for i in letters:
    if i.isalpha():
        count = text.count(i)
        if min_count_letter > count:
            min_count_letter = count
            min_i = i
        
        
print(f'Букв - {count_letter}\n'
      f'Слов - {count_word}\n'
      f'Cтрок - {count_string}\n'
      f'Буква "{min_i}" встречается реже всех, {min_count_letter} раз(а).')
