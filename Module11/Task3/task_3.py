from family import Child, Parent

print('Задача 3. Отцы, матери и дети\n')

children = [Child('Артём', 3, False, False),
            Child('Коля', 2, True, True)]

parent = Parent('Наталья', 25, children)

parent.print_info()
parent.calm_child(children[0])
parent.feed_child(children[1])
parent.print_info()