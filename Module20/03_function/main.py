def slicer(tpl, elem):
    if tpl.count(elem) == 1:
        return tpl[tpl.index(elem):]
    elif tpl.count(elem) == 0:
        return tuple()
    else:
        lst = list()
        for index, element in enumerate(tpl):
            if element == elem:
                lst.append(index)
            if len(lst) == 2:
                break
        return tpl[lst[0]:lst[1] + 1]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 6))
