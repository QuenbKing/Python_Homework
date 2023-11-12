class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        if isinstance(opponent, Warrior):
            opponent.health -= 20
            print(f'{self.name} атаковал {opponent.name}. У {opponent.name} осталось {opponent.health} HP')