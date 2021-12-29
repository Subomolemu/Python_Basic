def summa(*args, my_list=[]):
	for i in args:
		if isinstance(i, list):
			for index in i:
				summa(index)
		else:
			my_list.append(i)

	return sum(my_list)


print(summa([[1, 2, [3]], [1], 3]))
