class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()
    
    def is_ripe(self):
        if self.state == 3:
            return True
        return False
    
    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')
