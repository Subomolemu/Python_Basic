all_cells = int(input('Введите колличество клеток: '))
inefficiency = ''

for i in range(all_cells):
    print('Эффективнность', i + 1, 'клетки: ', end='')
    efficiency = int(input())
    if efficiency < i:
        inefficiency += str(efficiency) + ' '

print('\nНеподходящие значения:', inefficiency)
