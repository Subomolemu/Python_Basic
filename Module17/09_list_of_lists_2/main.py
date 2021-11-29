nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
open_nice_list = [number for x in nice_list for num in x for number in num]
print(open_nice_list)
