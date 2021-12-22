import random

num_list = [random.randint(0, 100) for x in range(10)]
print(f'Оригинальный список: {num_list}')

new_list = []
for num in range(0, len(num_list), 2):
    new_list.append((num_list[num], num_list[num + 1]))
print(new_list)

new_list.clear()

new_list = [(num_list[num], num_list[num + 1]) for num in range(0, len(num_list), 2)]
print(new_list)

new_list.clear()

even_list = [num_list[num] for num in range(0, len(num_list), 2)]
odd_list = [num_list[num] for num in range(1, len(num_list), 2)]
zip_list = zip(even_list, odd_list)
for i in zip_list:
    new_list.append(i)
print(new_list)