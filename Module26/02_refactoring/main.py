from collections.abc import Iterable


class Find:
    def __init__(self, lst_1: list, lst_2: list, num_find: int):
        self.lst_1 = lst_1
        self.lst_2 = lst_2
        self.num_find = num_find

    def __iter__(self) -> Iterable:
        return self
    
    def __next__(self) -> str:
        for x in list_1:
            for y in list_2:
                result = x * y
                print(x, y, result)
                if result == to_find:
                    return 'Found!!!'
        return 'Not found'


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 90

a = Find(lst_1=list_1, lst_2=list_2, num_find=to_find)
print(next(a))



