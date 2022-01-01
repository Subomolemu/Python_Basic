def return_list(lst):
    out_list = []
    for nested_value in lst:
        if not isinstance(nested_value, list):
            out_list.append(nested_value)
        else:
            out_list.extend(return_list(nested_value))
    return out_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(return_list(nice_list))

