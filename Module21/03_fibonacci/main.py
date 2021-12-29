def fib_num(num, it_num):
    if len(list_num) == num:
        return list_num[-1]
    list_num.append(it_num)
    return fib_num(num, it_num=list_num[-1] + list_num[-2])


list_num = [1]
iter_num = 1
number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'\nЧисло: {fib_num(number, iter_num)}')
