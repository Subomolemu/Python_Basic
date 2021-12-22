def f_zip(a, b):
    tpl = []
    if len(a) < len(b):
        for i in range(len(a)):
            tpl.append((a[i], b[i]))
        return tuple(tpl)
    else:
        for i in range(len(b)):
            tpl.append((a[i], b[i]))
        return tpl


string = 'abcd'
num_tpl = (10, 20, 30, 40)

lst = (i for i in zip(string, num_tpl))
print(lst)

for i in lst:
    print(i)

print(f_zip(string, num_tpl))
