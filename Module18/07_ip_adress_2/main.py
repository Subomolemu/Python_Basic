ip = True
ip_address = input('Введите ip - адрес: ')
if ip_address[-1] == '.':
    print('ip - адрес не должен заканчиваться точкой.')
    ip = False
if ip_address[0] == '.':
    print('ip - адрес не должен начинаться с точки.')
    ip = False

ip_address = ip_address.split('.')

for i in ip_address:

    if not i.isdigit():
        if i.isalnum():
            print('{} - не целое число.'.format(i))
        print('ip - адрес это 4 числа, разделенные точкой.')
        ip = False
        break
    elif int(i) > 255:
        print(i, '- превышает 255.')
        ip = False
        break

    if len(ip_address) < 4:
        print('Количество чисел в ip адресе меньше 4.')
        ip = False
        break
    elif len(ip_address) > 4:
        print('Количество чисел в ip адресе больше 4.')
        ip = False
        break

if ip:
    print('ip - адрес корректен.')
