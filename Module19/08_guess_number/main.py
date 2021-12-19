max_num = int(input('Введите максимальное число: '))
all_num_list = (str(x) for x in range(1, max_num + 1))
my_nums = input('Нужное число есть среди вот этих чисел: ').lower().split()
all_num_list = set(all_num_list)

while ''.join(my_nums) != 'помогите!':
    my_nums = set(my_nums)
    answer = input('Ответ Артема: ').lower()
    print()
    if answer == 'да':
        all_num_list &= my_nums
    else:
        all_num_list -= my_nums

    my_nums = input('Нужное число есть среди вот этих чисел: ').lower().split()

all_num_list = ' '.join(all_num_list)
sorted(all_num_list)
print()
print(f'Артём мог загадать следующие числа: {all_num_list}')
