import random
from warrior import Warrior

print('Задача 1. Драка\n')

warriors = [Warrior('Воин_1'), Warrior('Воин_2')]

while all(warrior.health > 0 for warrior in warriors):
    warrior_num = random.randint(0, len(warriors) - 1)
    attacker, opponent = warriors[warrior_num], warriors[abs(warrior_num - 1)]
    attacker.attack(opponent)
    if opponent.health == 0:
        print(f'Победил {attacker.name}')