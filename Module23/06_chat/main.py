import os


name = input('Введите имя пользователя: ')
chat = open('chat.txt', 'a', encoding='utf-8')
count = 0
    
if os.path.exists('count_post.log'):
    with open('count_post.log', 'r') as count_post:
        for num in count_post:
            if num.isalnum():
                count = int(num)
                
count_post = open('count_post.log', 'w')

while True:
    try:
        choice = int(input('\nВведите номер действия: '
                           '\n\t 1. Посмотреть текущий текст чата'
                           '\n\t 2. Отправить сообщение'
                           '\n\t 3. Закрыть чат'
                           '\n\t\t Ваш выбор: '))
    
        if choice not in (1, 2, 3):
            raise ValueError
        
        if choice == 1:
            chat.close()
            chat = open('chat.txt', 'r', encoding='utf-8')
            print('')
            for string in chat:
                print(f'{string}', end='')
                
            chat.close()
            chat = open('chat.txt', 'a', encoding='utf-8')
            
        elif choice == 2:
            
            count += 1
            count_post.seek(0)
            count_post.write(str(count))
            text = input('\nВведите сообщение: ')
            chat.write(f'{count}) {name}:  {text}\n')
            
        elif choice == 3:
            print(f'\nЗавершение работы чата для пользователя {name}...')
            break
            
    except ValueError:
        print('\nДля выбора необходимо ввести одну из трех цифр(1, 2, 3): ')
    except KeyboardInterrupt:
        print('\n------------------\nЭкстренное завершение чата пользователем.')
        break
        
count_post.close()
chat.close()
