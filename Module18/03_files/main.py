file_name = input('Введите название файла: ')
if not file_name.endswith('.txt') and not file_name.endswith('.dock'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    ban_sym = '@№$%^&*()'
    if file_name[0] in ban_sym:
        print('Ошибка: название начинается на один из специальных символов.')
    else:
        print('Файл назван верно.')
