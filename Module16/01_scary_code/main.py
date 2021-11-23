a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

for i in b:
    a.append(i)

print('Кол-во цифр 5 при первом объединении:', a.count(5))

for sym in a:
    if sym == 5:
        a.remove(5)

for i in c:
    a.append(i)

print('Колличество цифр 3 при втором объъединении:', a.count(3))
print(a)
