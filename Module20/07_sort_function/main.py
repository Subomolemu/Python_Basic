def tpl_sort(tpl):
    tpl = tuple(tpl)
    for i in tpl:
        if not isinstance(i, int):
            return tpl

    return tuple(sorted(tpl))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 4, 10.1, -5)))
