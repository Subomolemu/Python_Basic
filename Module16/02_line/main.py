first = list(range(160, 176, 2))
second = list(range(162, 180, 3))
for num in second:
    first.append(num)

first = sorted(first)
print(first)

# Изучаю книгу Эрика Мэтиза, решил попробовать метод сортировки оттуда. Если так делать на данном
# этапе нельзя, то переделаю
