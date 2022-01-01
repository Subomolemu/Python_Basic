def summa(*args):
	total = 0
	for i in args:
		if isinstance(i, (int, float)):
			total += i
		elif isinstance(i, list):
			for value in i:
				total += summa(value)
			
	return total


print(summa(1, 2, 3, 4, 5))
