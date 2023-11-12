import random

from home import Home


class Human:
    def __init__(self, name, home: Home):
        self.name = name
        self.satiety = 50
        self.home = home

    def eat(self):
        difference = min(20, self.home.meal)
        self.satiety += difference
        self.home.meal -= difference

    def work(self):
        self.satiety -= 20
        self.home.money += 50

    def play(self):
        self.satiety -= 15

    def go_to_the_store(self):
        difference = min(self.home.money, 40)
        self.home.meal += difference * 0.75
        self.home.money -= difference

    def live_the_day(self):
        num = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.meal < 10:
            self.go_to_the_store()
        elif self.home.money < 50 or num == 1:
            self.work()
        elif num == 2:
            self.eat()
        else:
            self.play()

    def print_info(self):
        print(f'Имя: {self.name}\nСытость: {self.satiety}\n')
