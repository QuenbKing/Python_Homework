class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return f'{self.__class__.__name__} высота: {self.height}, скорость: {self.speed}'


class Butterfly(CanFly):
    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):

    def take_off(self):
        self.height = 500
        self.speed = 1000

    def landing(self):
        self.height = 0
        self.boom()

    def boom(self):
        print('Всё взорволося')