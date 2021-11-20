total_graphics_cards = int(input('Введите колличество видеокарт: '))
cards_list = []
new_cards = 0
new_cards_list = []

for num in range(total_graphics_cards):
    print(num + 1, 'видеокарта: ', end='')
    graphics_card = int(input())
    cards_list.append(graphics_card)
    if new_cards < graphics_card:
        new_cards = graphics_card


print('\nСтарый список видеокарт:', cards_list)

for cards in cards_list:
    if cards != new_cards:
        new_cards_list.append(cards)

print('Новый список видеокарт:', new_cards_list)
