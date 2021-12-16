max_num = int(input('Введите максимальное число: '))
all_num_list = [str(x) for x in range(1, max_num + 1)]
my_nums = input('Нужное число есть среди вот этих чисел: ').lower().split()
check_num_list = []
check_num_list.extend(all_num_list)
while ''.join(my_nums) != 'помогите!':
    answer = input('Ответ Артема: ').lower()
    print()
    if answer == 'нет':
        for num in my_nums:
            if num in check_num_list:
                check_num_list.remove(num)
            else:
                continue

    if answer == 'да':
        for num in all_num_list:
            if num not in my_nums:
                check_num_list.remove(num)
            else:
                continue

    my_nums = input('Нужное число есть среди вот этих чисел: ').lower().split()

print()
check_num_list = ' '.join(check_num_list)
print(f'Артём мог загадать следующие числа: {check_num_list}')



