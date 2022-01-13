import random


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
            if string[1] == '+':
                result = string[0] + string[2]
            elif string[1] == '-':
                result = string[0] - string[2]
            elif string[1] == '/':
                result = string[0] / string[2]
            elif string[1] == '*':
                result = string[0] * string[2]
            elif string[1] == '//':
                result = string[0] // string[2]
            elif string[1] == '%':
                result = string[0] % string[2]
            total_sum += result
        except ZeroDivisionError:
            print('На ноль делить нельзя.')
        except ValueError:
            print('Это калькулятор, давай без букв.')
        except TypeError:
            print('Мне кажется в калькулятор зайдут только цифры...')
print(f'\nСумма результатов выполненных {total_sum}')
