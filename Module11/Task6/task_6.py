from game import *

print('Задача 6. Крестики-нолики\n')

player_1 = Player('Игрок 1', 'X')
player_2 = Player('Игрок 2', 'O')

game = Game([player_1, player_2])

game.start_game()