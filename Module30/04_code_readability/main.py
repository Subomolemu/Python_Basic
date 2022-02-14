from typing import List


def import_list() -> List:
    lst = list()
    for i in range(1001):
        lst.append(i)
    return lst


print(list(map(lambda x: x, [x for x in range(1001)])))

print(import_list())

print(list(x for x in range(1001)))  # самый простой и читаемый, как по мне
