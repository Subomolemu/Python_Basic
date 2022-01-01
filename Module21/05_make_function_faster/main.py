def calculating_math_func(data, data_dict):
    result = 1
    
    if data in data_dict:
        return data_dict[data]
    
    for index in range(1, data + 1):
        result *= index
        
        if index in data_dict:
            continue
        else:
            data_dict[index] = result
            
    result /= data ** 3
    result = result ** 10
    
    return result


my_dict = {}
number = int(input('Введите число:'))
print(calculating_math_func(number, my_dict))

number = int(input('Введите число:'))
print(calculating_math_func(number, my_dict))
