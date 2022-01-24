import random


class TicTacToe:
    row_list = [0, 2, 4, 6]
    col_list = [0, 4, 8, 12]
    sym_list = [2, 6, 10]
    x_sym = []
    o_sym = []
    stat_x = 0
    stat_o = 0
    win_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                       [2, 5, 8], [3, 5, 9], [1, 5, 9], [3, 5, 7]]

    def __init__(self, name):
        self.name = name
    
    def take_a_field(self):
        x_o_list = self.x_sym + self.o_sym
        cell_number = 0
        for row in range(7):
            if row in self.row_list:
                for col in range(13):
                    print('=', end='')
            else:
                for col in range(13):
                    if col in self.col_list:
                        print('|', end='')
                    elif col in self.sym_list:
                        cell_number += 1
                        
                        if cell_number not in x_o_list:
                            print(cell_number, end='')
                        elif cell_number in self.x_sym:
                            print('X', end='')
                        elif cell_number in self.o_sym:
                            print('0', end='')
                    else:
                        print(' ', end='')
            print('')
            
    def start_game(self):
        while True:
            move_pc = random.randint(1, 10)
            move_player = random.randint(1, 10)
            
            if move_player > move_pc:
                print(f'{self.name} начинает игру. Он играет за крестики.')
                self.take_a_field()
                self.mode_o_pc()
                break
                
            elif move_player < move_pc:
                print('Компьютер начинает игру. Он играет за крестики.')
                self.mode_x_pc()
                break
    
    def mode_x_pc(self):
        self.x_sym.append(5)
        while True:
            self.take_a_field()
            x_o_list = self.x_sym + self.o_sym
            print(x_o_list)
            print(self.x_sym)
            print(self.o_sym)
            player_move = int(input('Введите номер клетки, куда ставить '
                                    '"О":'))
            
            if 0 < player_move < 10:
                if player_move not in x_o_list:
                    self.o_sym.append(player_move)
                else:
                    print(f'В клетку номер {player_move} сделать свой ход '
                          f'нельзя')
                    continue
                    
            if self.check_win_o():
                self.take_a_field()
                print(f'{self.name} выиграл!')
                break
                
            while True:
                pc_move = random.randint(1, 9)
                if pc_move not in x_o_list:
                    self.x_sym.append(pc_move)
                    print('Компьютер сделал свой ход')
                    self.take_a_field()
                    if self.check_win_x():
                        print('Выиграл компьютер!')
                        break
                break

    def mode_o_pc(self):
        while True:
            x_o_list = self.x_sym + self.o_sym
            print(x_o_list)
            print(self.x_sym)
            print(self.o_sym)
            x_o_list = self.x_sym + self.o_sym
            player_move = int(input('Введите номер клетки, куда ставить '
                                    '"X":'))
            if 0 < player_move < 10:
                if player_move not in x_o_list:
                    self.x_sym.append(player_move)
                else:
                    print(f'В клетку номер {player_move} сделать свой ход '
                          f'нельзя')
                    continue
                    
            if self.check_win_x():
                self.take_a_field()
                print(f'{self.name} выиграл!')
                break
                
            while True:
                pc_move = random.randint(1, 9)
                if pc_move not in x_o_list:
                    self.o_sym.append(pc_move)
                    print('Компьютер сделал свой ход')
                    self.take_a_field()
                    
                    if self.check_win_o():
                        self.take_a_field()
                        print('Выиграл компьютер!')
                        break
                break

    def check_win_o(self):
        for comb in self.win_combination:
            if comb == sorted(self.o_sym):
                return True
        return False
        
    def check_win_x(self):
        for comb in self.win_combination:
            if comb == sorted(self.x_sym):
                return True
        return False
