def find_error_in_string(string):
    if len(string) < 3:
        raise IndexError
    elif not string[0].isalpha():
        raise NameError
    elif ('@' not in string[1]) and ('.' not in string[1]):
        raise SyntaxError
    elif 100 < int(string[2]) < 9:
        raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as registrations, open(
          'registrations_bad.log', 'w', encoding='utf-8') as bad, open(
          'registrations_good.log', 'w', encoding='utf-8') as good:
    
    for i_string in registrations:
        check_string = i_string.split()
        try:
            find_error_in_string(check_string)
            good.write(i_string)
            
        except IndexError:
            check_string = ' '.join(check_string)
            bad.write(f'{check_string} - НЕ присутствуют все три '
                      f'поля\n')
        except NameError:
            check_string = ' '.join(check_string)
            bad.write(f'{check_string} - поле имени содержит НЕ только буквы\n')
        except SyntaxError:
            check_string = ' '.join(check_string)
            bad.write(f'{check_string} - поле емейл НЕ содержит @ и .(точку)\n')
        except ValueError:
            check_string = ' '.join(check_string)
            bad.write(f'{check_string} - поле возраст НЕ является числом от '
                      f'10 до 99\n')
    