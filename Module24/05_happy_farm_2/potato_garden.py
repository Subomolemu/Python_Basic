import potato


class PotatoGarden:
    
    def __init__(self, count):
        self.potatoes = [potato.Potato(index) for index in range(1, count + 1)]
    
    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()
    
    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела.\n')
            return False
        return True
    