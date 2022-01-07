import os


def file_contents(path):
    print('\nСодержимое файла:')
    file = open(path, 'r')
    for i in file:
        print(i)
    file.close()


def working_with_file(ans):
    if ans:
        new_file = open(check_path, 'w')
        new_file.write(string)
        print('Файл успешно перезаписан.')
        new_file.close()
    
        file_contents(check_path)
    else:
        new_file = open(check_path, 'w')
        new_file.write(string)
        print('Файл успешно сохранен.')
        new_file.close()
    
        file_contents(check_path)


string = input('Введите строку: ')
input_path = input('Куда хотите сохранить документ? Введите последовательность '
                   'папок (через пробел):').lower().split()
input_path = '/'.join(input_path)
abs_path = os.path.abspath(os.path.join(os.path.sep, input_path))

if os.path.exists(abs_path):
    file_name = input('Введите имя файла: ')
    check_path = os.path.join(abs_path, file_name + '.txt')
    
    if os.path.exists(check_path):
        answer = input('Вы действительно хотите перезаписать файл? ')\
            .strip().lower()
        if answer == 'да':
            working_with_file(answer)
        else:
            print('Работа завершена.')
    else:
        working_with_file(ans=None)
        
else:
    print('Такого пути не существует.')
    