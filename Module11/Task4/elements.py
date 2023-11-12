class Water:
    def __init__(self):
        self.title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            return None


class Air:
    def __init__(self):
        self.title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None


class Fire:
    def __init__(self):
        self.title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ground):
            return Lava()
        else:
            return None


class Ground:
    def __init__(self):
        self.title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    def __init__(self):
        self.title = 'Шторм'

    def __add__(self, other):
        return None


class Steam:
    def __init__(self):
        self.title = 'Пар'

    def __add__(self, other):
        return None


class Dirt:
    def __init__(self):
        self.title = 'Грязь'

    def __add__(self, other):
        return None


class Lightning:
    def __init__(self):
        self.title = 'Молния'

    def __add__(self, other):
        return None


class Dust:
    def __init__(self):
        self.title = 'Пыль'

    def __add__(self, other):
        return None


class Lava:
    def __init__(self):
        self.title = 'Лава'

    def __add__(self, other):
        return None
