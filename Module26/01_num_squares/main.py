from collections.abc import Iterator


class NumSquare:
    def __init__(self, num: int):
        self.start_num = 0
        self.num = num
        
    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self) -> int:
        if self.start_num != self.num:
            self.start_num += 1
            return self.start_num ** 2
        raise StopIteration
    
    
def num_square(num: int):
    start_num = 0
    while True:
        if start_num != num:
            start_num += 1
            yield start_num ** 2
        else:
            break
    
    
my_number = int(input('Введите конечное число: '))

for number in NumSquare(num=my_number):
    print(number, end=' ')
    
print('\n')

for number in num_square(num=my_number):
    print(number, end=' ')
    
print('\n')

number = [num**2 for num in range(1, my_number + 1)]
for num in number:
    print(num, end=' ')