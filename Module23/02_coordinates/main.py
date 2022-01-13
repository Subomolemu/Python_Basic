import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'w') as coordinates:
    for _ in range(5):
        random_numbers = f'{random.randint(10, 100)} ' \
                         f'{random.randint(10, 100)}'
        coordinates.write(f'{random_numbers}\n')
        
with open('coordinates.txt', 'r') as coordinates:
    with open('result.txt', 'w') as result:
        for i_line, line_number in enumerate(coordinates):
            nums_list = line_number.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                
                my_list = sorted([res1, res2, number])
                str_list = [str(round(num, 3)) for num in my_list]
                result.write(f'{" ".join(str_list)}\n')
            except ZeroDivisionError:
                print(f'Ошибка в {i_line + 1} строке.')
