total_number = int(input('Количество чисел: '))
num_list = []
revers_list = []
count = 0
added_num = []

for _ in range(total_number):
    number = int(input('Число: '))
    num_list.append(number)

num_list.reverse()
revers_list.extend(num_list)
num_list.reverse()

print('Последовательность: ', end='')
for num in num_list:
    print(num, end=' ')


for i in range(len(num_list)):

    if num_list[i] != revers_list[i - count]:
        added_num.append(num_list[i])
        count += 1
        num_list.insert(len(revers_list), num_list[i])

print('Нужно приписать чисел:', count)
print('Эти числа:', end=' ')

for num in num_list:
    print(num, end=' ')
