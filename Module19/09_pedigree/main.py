total_people = int(input('Введите количество человек: '))
tree = {}

for i in range(1, total_people):
    child, parent = input(f'{i} пара: ').split()
    if parent not in tree:
        tree[parent] = 0
    if child not in tree:
        tree[child] = tree[parent] + 1

print('\nВысота каждого члена семьи: ')
for person, lvl in sorted(tree.items()):
    print(f'{person} {lvl}')
