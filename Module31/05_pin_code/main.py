import itertools


num_list = [a for a in range(0, 10)]
for item in itertools.combinations(num_list, 4):
    print(item)