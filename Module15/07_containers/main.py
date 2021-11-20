total_containers = int(input('Введите колличество контейнеров: '))
weight_containers = []

for _ in range(total_containers):
    weight_container = int(input('Введите вес контейнера: '))
    while weight_container <= 0 or weight_container > 200:
        print('Ошибка ввода. Вес контейнера должен быть больше 0 и не превышать 200.\n')
        weight_container = int(input('Введите вес контейнера: '))
    weight_containers.append(weight_container)

print()
new_container = int(input('Введите вес нового контейнера: '))
while new_container <= 0 or new_container > 200:
    print('Ошибка ввода. Вес контейнера должен быть больше 0 и не превышать 200.\n')
    new_container = int(input('Введите вес нового контейнера: '))

print()
for i in range(len(weight_containers)):
    if weight_containers[i] < new_container:
        print('Номер, куда встанет новый контейнер:', i + 1)
        break
