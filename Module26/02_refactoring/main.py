def find_result(lst_1, lst_2, num_find):
    for x in lst_1:
        for y in lst_2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == num_find:
                print('Found!!!')
                raise StopIteration # если вместо raise написать return,
                # то возврат значений закончится без ошибок, и код продолжит
                # выполняться, или это неправильно?


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

gen = find_result(lst_1=list_1, lst_2=list_2, num_find=to_find)
print(gen)
for i in gen:
    print(i)