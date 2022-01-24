import blackjack

game = blackjack.Blackjack('Сергей')
game.start_play()
game.check_cards()

while True:
    answer = input('\nВзять карту?(1)\n'
                   'Остановиться?(0)\n'
                   '\tВаш ответ(1/0):')
    print()
    
    if answer == '0':
        game.stop_play()
        break
    elif answer == '1':
        game.dealing_cards()
        game.check_cards()
        if game.player_points > 21:
            print('У вас на руках больше 21 очков. Пора заканчивать.')
            game.stop_play()
            break
        