shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Название детали: ')
price_details = 0
count = 0

for detail in shop:
    if detail[0] == detail_name:
        price_details += detail[1]
        count += 1

print('Колличество деталей:', count)
print('Общая стоимость:', price_details)

