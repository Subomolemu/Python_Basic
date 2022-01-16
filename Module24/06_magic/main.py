class Water:
    def __add__(self, other):
        if other == Wind:
            return Storm
        elif other == Fire:
            return Steam
        elif other == Earth:
            return Mud

    
class Fire:
    def __add__(self, other):
        if other == Wind:
            return Lightning
        elif other == Water:
            return Steam
        elif other == Earth:
            return Lava


class Wind:
    def __add__(self, other):
        if other == Water:
            return Storm
        elif other == Fire:
            return Lightning
        elif other == Earth:
            return Dust
        

class Earth:
    def __add__(self, other):
        if other == Wind:
            return Dust()
        elif other == Fire:
            return Lava()
        elif other == Water:
            return Mud()
    
        
class Storm(Water, Wind):
    answer = 'При сложении воды и воздуха возник новый элемент - шторм!'
    
    
class Lava(Fire, Earth):
    answer = 'При сложении земли и огня возник новый элемент - лава!'
    

class Mud(Earth, Water):
    answer = 'При сложении земли и воды возник новый элемент - грязь!'
    
    
class Dust(Earth, Wind):
    answer = 'При сложении земли и ветра возник новый элемент - пыль!'
    
    
class Lightning(Wind, Fire):
    answer = 'При сложении огня и ветра возник новый элемент - молния!'
    
    
class Steam(Fire, Water):
    answer = 'При сложении воды и огня возник новый элемент - пар!'


res = Fire() + Water
print(res.answer)

res_1 = Wind() + Earth
print(res_1.answer)

res_2 = Fire() + Steam
print(res_2)
