def f_zip(a, b):
    min_len = min(len(a), len(b))
    tpl = ((a[i], b[i]) for i in range(min_len))
    return tpl


string = 'abc'
num_tpl = (10, 20, 30, 40)

lst = (i for i in zip(string, num_tpl))
print(lst)

for i in lst:
    print(i)

print(f'\n{f_zip(string, num_tpl)}')
for i in f_zip(string, num_tpl):
    print(i)