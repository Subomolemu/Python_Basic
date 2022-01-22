class Water:
    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm
        elif isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Mud

    
class Fire:
    def __add__(self, other):
        if isinstance(other, Wind):
            return Lightning
        elif isinstance(other, Water):
            return Steam
        elif isinstance(other, Earth):
            return Lava


class Wind:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm
        elif isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Earth):
            return Dust
        

class Earth:
    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust
        elif isinstance(other, Fire):
            return Lava
        elif isinstance(other, Water):
            return Mud
    
        
class Storm:
    answer = 'При сложении воды и воздуха возник новый элемент - шторм!'
    
    
class Lava:
    answer = 'При сложении земли и огня возник новый элемент - лава!'
    

class Mud:
    answer = 'При сложении земли и воды возник новый элемент - грязь!'
    
    
class Dust:
    answer = 'При сложении земли и ветра возник новый элемент - пыль!'
    
    
class Lightning:
    answer = 'При сложении огня и ветра возник новый элемент - молния!'
    
    
class Steam:
    answer = 'При сложении воды и огня возник новый элемент - пар!'


try:
    a = Fire()
    b = Water()
    res = a + b
    print(res.answer)
    
    a = Wind()
    b = Earth()
    res_1 = a + b
    print(res_1.answer)
    
    a = Fire()
    b = Steam()
    res_2 = a + b
    print(res_2.answer)
    
except AttributeError:
    print(None)
    