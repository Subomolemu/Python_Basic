def return_list(lst, out_list=[]):
    if isinstance(lst, list):
        for i in lst:
            if isinstance(i, list):
                for index in i:
                    return_list(index)

            else:
                out_list.append(i)
    return out_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(return_list(nice_list))
