num = int(input('Введите колличество элементов в списке: '))
shift = int(input('Введите значение сдвига: '))
numbers = []
shift_numbers = []

for _ in range(num):
    number = int(input('Введите элемент списка: '))
    numbers.append(number)

print('Изначальный список: ', numbers)

for i in range(-shift, num - shift):
    shift_numbers.append(numbers[i])

print('Сдвинутый список:', shift_numbers)
