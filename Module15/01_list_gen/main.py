number = int(input('Введите число: '))
odd_nums = []

for num in range(1, number + 1):
    if num % 2 != 0:
        odd_nums.append(num)

print(odd_nums)
