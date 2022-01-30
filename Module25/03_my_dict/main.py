class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)
        
        
my_dict = MyDict()
my_dict[2] = 1
my_dict[3] = 3
print(my_dict)
print(my_dict.get(1))
