class Warrior:
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def get_punch(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            