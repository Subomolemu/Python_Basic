def add_contact():
    name, surname = input('Введите имя и фамилию нового контакта '
                          '(через пробел): ').strip().lower().title().split()
    for key in number_book.keys():
        if name in key and surname in key:
            print('Такой человек уже есть в контактах.')
            print(f'Текущий словарь контактов: {number_book}\n')
            return

    tel_number = int(input('Введите номер телефона: '))
    number_book[(name, surname)] = tel_number
    print(f'Текущий словарь контактов: {number_book}\n')


def find_contact():
    flag = False
    surname = input('Введите фамилию для поиска: ').strip().lower().title()

    for contact, number in number_book.items():
        if contact[1] == surname:
            print(f'{contact[0]} {contact[1]}: {number}')
            flag = True

    print(f'Текущий словарь контактов: {number_book}\n')
    if not flag:
        print('Такой человек не найден.')


number_book = {}

while True:
    print('Введите номер действия: \n 1. Добавить контакт \n 2. Найти человека ')
    choice = input('- ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        find_contact()
    else:
        print('Ошибка ввода при выборе действия\n')