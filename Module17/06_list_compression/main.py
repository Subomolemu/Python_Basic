import random

num = int(input('Введите длину списка чисел: '))

numbers = [random.randint(0, 5) for _ in range(num)]
print(numbers)

shift = [(x if x != 0 else numbers.append(numbers.pop(numbers.index(x)))) for x in
         numbers]
print(numbers)

while numbers[-1] == 0:
    numbers.remove(numbers[-1])
print(numbers)
