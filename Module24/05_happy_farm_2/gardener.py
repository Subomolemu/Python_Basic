import potato_garden


class PotatoGardener:
    
    def __init__(self, name, i_potato):
        self.name = name
        self.garden = potato_garden.PotatoGarden(i_potato)
    
    def garden_care(self):
        while True:
            if self.garden.are_all_ripe():
                print('Вся картошка созрела. Можно собрать!\n')
                break
            self.garden.grow_all()
            continue
    
    def harvest(self):
        bucket = []
        if self.garden.are_all_ripe():
            print(f'В корзину собрано {len(self.garden.potatoes)} плод(а)')
            for i_potato in self.garden.potatoes:
                bucket.append(f'{i_potato.index} картошка - '
                              f'{i_potato.states[i_potato.state]}', )
        return bucket
    