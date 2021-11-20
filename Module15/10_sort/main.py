def sort_numbers(list_nums):
    for min_i in range(len(list_nums)):
        for current in range(min_i, len(list_nums)):
            if list_nums[current] < list_nums[min_i]:
                list_nums[current], list_nums[min_i] = list_nums[min_i], list_nums[current]


n = int(input('Введите колличество элементов в списке: '))
numbers = []

for _ in range(n):
    num = int(input('Введите число: '))
    numbers.append(num)

print('=' * 20, '\nИзначальный список:', numbers)
sort_numbers(numbers)
print('\nОтсортированный список', numbers)
