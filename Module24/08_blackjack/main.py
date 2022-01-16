import random


def random_card():
    stop = random.randint(1, len(BlackJack.cards_dict))
    for i, key in enumerate(BlackJack.cards_dict):
        if i == stop:
            return key


def start_play(def_player, def_dealer):
    for _ in range(2):
        if def_player.points <= 21:
            BlackJack.cards_dict['ace'] = 11
            
            card = random_card
            def_player.cards.append(card)
        else:
            card = random_card
            def_player.cards.append(card)
            
        if def_dealer.points <= 21:
            BlackJack.cards_dict['ace'] = 11
            
            card = random_card
            def_dealer.cards.append(card)
        else:
            card = random_card
            def_dealer.cards.append(card)
        

def check_points(player_point, dealer_point):
    if player_point > 21:
        print(f'К сожалению игрок проиграл. Он набрал {player_point} очков.')
    elif player_point == 21:
        print(f'Игрок выиграл, он набрал ровно {player_point} очков!')
    elif player_point > dealer_point:
        print(f'Игрок выиграл, он набрал {player_point} очков\n '
              f'Дилер набрал {dealer_point} очков')
    elif player_point < dealer_point:
        print(f'Дилер выиграл, он набрал {dealer_point} очков\n '
              f'Игрок набрал {player_point} очков')
    else:
        print(f'Вышла ничья!\n'
              f'У игрока {player_point} очков\n'
              f'у дилера {dealer_point} очков\n')
        
        
def take_card(def_player, def_dealer):
    card = random.choice(BlackJack.cards_dict)
    def_player.cards.append(card)
    def_dealer.cards.append(card)


class Player:
    points = 0
    cards = []
    name = ''
    
    def __init__(self, name):
        self.name = name
    
    def see_points(self):
        for num in self.cards:
            self.points += BlackJack.cards_dict[num]
        print(f'У игрока {self.name} {self.points} очков.')
        return self.points


class Dealer:
    points = 0
    cards = []
    
    def __init__(self, name):
        self.name = name
        
    def see_points(self):
        for num in self.cards:
            self.points += num
        print(f'У дилера {self.points} очков.')
        return self.points


class BlackJack:
    
    cards_dict = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                  'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                  'jack': 10, 'dame': 10, 'king': 10, 'ace': 1}


im = Player('Sergey')
dl = Dealer('Dealer')

start_play(im, dl)

while True:
    im.see_points()
    for card in im.cards:
        print({BlackJack.cards_dict[card]})

    choice = input('Выберите действие:\n'
                   '\t1)Взять карту\n'
                   '\t2)Остановиться\n'
                   '\tВаш выбор: ')
    if choice == '1':
        take_card(im, dl)
    elif choice == '2':
        check_points(im.points, dl.points)
        break
        