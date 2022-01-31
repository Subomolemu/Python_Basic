class QHofstadter:
    def __init__(self, s):
        self.s = s

    def __iter__(self):
        return self

    def __next__(self):
        if self.s == [1, 2]:
            raise StopIteration
        else:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q


q = QHofstadter([1, 1])
for i in range(10):
    print(next(q))