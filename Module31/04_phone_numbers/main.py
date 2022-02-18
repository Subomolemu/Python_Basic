import re


num_list = ['9999999999', '999999-999', '99999x9999']
for i, num in enumerate(num_list):
    date = re.findall(r'[8,9]\d{9}', num)
    if num in date:
        print(f'{i + 1} номер: всё в порядке')
    else:
        print(f'{i + 1} номер: не подходит')