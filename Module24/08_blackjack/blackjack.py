import random


class Blackjack:
    dealer_cards = []
    dealer_points = 0
    
    player_cards = []
    player_points = 0
    
    card_dict = {1: ['two', 2], 2: ['three', 3], 3: ['four', 4],
                 4: ['five', 5], 5: ['six', 6], 6: ['seven', 7],
                 7: ['eight', 8], 8: ['nine', 9], 9: ['ten', 10],
                 10: ['valet', 10], 11: ['dama', 10], 12: ['king', 10],
                 13: ['ace', 11]}
    
    def __init__(self, name):
        self.name = name
    
    def check_dealer_points(self):
        self.dealer_points = 0
        for i in self.dealer_cards:
            self.dealer_points += i[1]
         
    def check_player_points(self):
        self.player_points = 0
        for i in self.player_cards:
            self.player_points += i[1]
        
    def start_play(self):
        for i in range(2):
            self.dealing_cards()
    
    def dealing_cards(self):
        if self.player_points > 21:
            self.card_dict[13] = ['ace', 1]
        while True:
            card = self.card_dict[random.randint(1, 13)]
            if card in self.player_cards:
                continue
            break
        self.player_cards.append(card)
        self.card_dict[13] = ['ace', 1]
        self.check_player_points()
        
        if self.dealer_points > 21:
            self.card_dict[13][1] = 1
        while True:
            card = self.card_dict[random.randint(1, 13)]
            if card in self.dealer_cards:
                continue
            break
        self.dealer_cards.append(card)
        self.card_dict[13][1] = 11
        
    def stop_play(self):
        
        if self.player_points <= 21:
            if self.player_points > self.dealer_points:
                print(f'Игрок с ником {self.name} победил!')
            elif self.player_points == self.dealer_points:
                print(f'Ничья! Игрок с ником {self.name} и дилер набрали '
                      f'равное количество очков!')
            else:
                print(f'К сожалению игрок с ником {self.name} проиграл.')
        else:
            print(f'К сожалению игрок с ником {self.name} проиграл.')
        print(f'\tУ игрока с ником {self.name} {self.player_points} очков.\n'
              f'\tУ дилера {self.dealer_points} очков.')
        
    def check_cards(self):
        print(f'Ваши карты, {self.name}:')
        for i in self.player_cards:
            print(f'\t-{i[0]}({i[1]} очков)')
        self.check_dealer_points()
   