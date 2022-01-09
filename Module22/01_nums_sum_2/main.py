numbers = open('numbers.txt', 'r')
summa = 0
numbers = numbers.read().split()
for i in numbers:
	summa += int(i)

answer = open('answer.txt', 'w')
answer.write(str(summa))
print(answer)
answer.close()


