def sum_number(num, nums):
    while num > 0:
        nums += num % 10
        num //= 10
    print('Сумма цифр:', nums)
    return nums


def count_number(num, count_num):
    while num > 0:
        num //= 10
        count_num += 1
    print('Колличество цифр:', count_num)
    return count_num


number = int(input('Введите число:'))
count = 0
sumNum = 0

print()
print('Разность суммы и колличества цифр:', sum_number(number, sumNum) - count_number(number, count))
