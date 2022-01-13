import random


def raise_choice():
    errors = [SystemError, TypeError, ValueError, UnicodeError]
    return random.choice(errors)


def file_output(file):
    print('Содержимое файла out_file.txt:')
    for i in file:
        print(f'{i}', end='')


total_sum = 0

print('Вводите числа для записи в файл, пока их сумма не окажется >= 777')
out_file = open('out_file.txt', 'w')
while total_sum < 777:
    entered_number = int(input('Введите число: '))
    total_sum += entered_number
    try:
        x = random.randint(1, 13)
        if x == 7:
            raise raise_choice()
        out_file.write(f'{str(entered_number)}\n')
        if total_sum >= 777:
            out_file.close()
            with open('out_file.txt', 'r') as out_file:
                print('\nВы успешно выполнили условие, для выхода из '
                      'порочного цикла!\n')
                file_output(out_file)
    except (SystemError, TypeError, ValueError, UnicodeError):
        out_file.close()
        with open('out_file.txt', 'r') as out_file:
            print('Вас постигла неудача!')
            file_output(out_file)
        raise
            