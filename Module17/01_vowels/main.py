text = 'Нужно отнести кольцо в Мордор!'
vowels = 'ауоыиэяюёе'
vowels_in_text = [x for x in text if x in vowels]
print('Список гласных букв:', vowels_in_text)
print('Длина списка:', len(vowels_in_text))
