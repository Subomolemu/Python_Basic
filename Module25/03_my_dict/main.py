class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, i):
        if i in MyDict.keys(self):
            for key, value in MyDict.items(self):
                if key == i:
                    return value
        else:
            return 0

            
my_dict = MyDict()
my_dict[2] = 1
my_dict[3] = 3
print(my_dict)
print(my_dict.get(1))



