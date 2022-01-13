import random


def operation_selection(str_num):
    if str_num[1] == '+':
        res = str_num[0] + str_num[2]
    elif str_num[1] == '-':
        res = str_num[0] - str_num[2]
    elif str_num[1] == '/':
        res = str_num[0] / str_num[2]
    elif str_num[1] == '*':
        res = str_num[0] * str_num[2]
    elif str_num[1] == '//':
        res = str_num[0] // str_num[2]
    elif str_num[1] == '%':
        res = str_num[0] % str_num[2]
    else:
        raise TypeError
    return res
    
    
total_sum = 0
with open('calc.txt', 'w') as calc:
    calc.write(f'[] '
               f'+ {str(random.randint(0, 100))}\n')
    calc.write(f'{str(random.randint(0, 100))} '
               f'- {str(random.randint(0, 100))}\n')
    calc.write(f'{str(random.randint(0, 100))} '
               f'/ 0\n')
    calc.write(f'{str(random.randint(0, 100))} '
               f'* {str(random.randint(0, 100))}\n')
    calc.write(f'{str(random.randint(0, 100))} '
               f'// {str(random.randint(0, 100))}\n')
    calc.write(f'a '
               f'% {str(random.randint(0, 100))}\n')

with open('calc.txt', 'r') as calc:
    for i_string in calc:
        string = i_string.split()
        try:
            string = [int(x) if x.isalnum() else x for x in string]
            result = operation_selection(string)
            total_sum += result
        except (ZeroDivisionError, ValueError, TypeError):
            string = ' '.split()
            try:
                choice = input(f'Обнаружена ошибка в строке: {i_string}'
                               f'\tХотите исправить? (да/нет):').lower().strip()
                if choice == 'да':
                    fix_string = input('\nВведите исправленную '
                                       'строку: ').split()
                    fix_string = [int(x) if x.isalnum() else x for
                                  x in fix_string]
                    result = operation_selection(fix_string)
                    total_sum += result
                else:
                    continue
            except KeyboardInterrupt:
                print('\n--------------\nЭкстренное завершение работы '
                      'программы пользователем.')
                break
            
print(f'\nСумма результатов выполненных {total_sum}')
