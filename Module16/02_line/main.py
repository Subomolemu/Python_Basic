def sort_numbers(list_nums):
    for min_i in range(len(list_nums)):
        for current in range(min_i, len(list_nums)):
            if list_nums[current] < list_nums[min_i]:
                list_nums[current], list_nums[min_i] = list_nums[min_i], list_nums[current]


first = list(range(160, 176, 2))
second = list(range(162, 180, 3))
for num in second:
    first.append(num)

sort_numbers(first)
print(first)


