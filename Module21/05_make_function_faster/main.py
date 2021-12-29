def calculating_math_func(my_list, data):
    for index in range(1, data + 1):
        my_list[0] *= index
    my_list[0] /= data ** 3
    my_list[0] = my_list[0] ** 10


result = [1]
d = 5
calculating_math_func(result, d)
print(result[0])
