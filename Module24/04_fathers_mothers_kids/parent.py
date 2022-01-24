class Parent:
    
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children
    
    def info(self):
        print(f'\nМеня зовут {self.name}.\n'
              f'Мне {self.age} лет.')
        if len(self.children) > 0 and isinstance(self.children, list):
            
            if len(self.children) == 1:
                print('У меня есть ребенок, его зовут: ', end='')
            else:
                print('У меня есть дети, их зовут: ', end='')
            
            for i, child in enumerate(self.children):
                if i + 1 != len(self.children):
                    print(f'{child[0]}, {child[1]} лет; ', end='')
                else:
                    print(f'{child[0]}, {child[1]} лет.')
        else:
            print('У меня нет детей.')
    
    def check_relax(self):
        for i in range(len(self.children)):
            if self.children[i][2]:
                print(f'{self.children[i][0]}, я вижу что все хорошо, '
                      f'иди поиграй.')
            else:
                print(f'{self.children[i][0]}, ты переживаешь, давай обниму.')
                self.children[i][2] = True
    
    def check_hunger(self):
        for i in range(len(self.children)):
            if self.children[i][3]:
                print(
                    f'{self.children[i][0]}, не хочешь кушать? Пойдем играть.')
            else:
                print(f'{self.children[i][0]}, идем скорее кушать!.')
                self.children[i][3] = True
