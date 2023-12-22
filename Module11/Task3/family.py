class Child:
    def __init__(self, name, age, calm, hungry):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry

    def get_info(self):
        return (f'Имя: {self.name}, '
                f'Возраст: {self.age}, '
                f'Состояние спокойствия: {self.calm}, '
                f'Состояние голода: {self.hungry}')


class Parent:
    def __init__(self, name, age, children: list[Child]):
        self.name = name
        self.age = age
        self.children = children

    def print_info(self):
        print('Имя: {}\nВозраст: {}\nДети:\n{}\n'.format(self.name,
                                                         self.age,
                                                         "\n".join([i_child.get_info() for i_child in self.children])))

    def calm_child(self, child):
        if child in self.children and not child.calm:
            child.calm = True

    def check_valid_age(self):
        return all(self.age - child.age >= 16 for child in self.children)

    def feed_child(self, child):
        if child in self.children and child.hungry:
            child.hungry = False
