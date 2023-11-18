class Node:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node


class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
        self.current_iterator = self.head

    def append(self, value):
        node = Node(value)
        if self.count == 0:
            self.head = self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
        self.count += 1

    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError

        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.get_next()
        return cur_node.get_data()

    def remove(self, index):
        if index < 0 or index >= self.count:
            raise IndexError

        if index == 0:
            self.head = self.head.get_next()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.get_next()
            current.set_next(current.get_next().get_next())
            if index == self.count - 1:
                self.tail = current
        self.count -= 1

    def __str__(self):
        return f"[{', '.join(str(el) for el in self)}]"

    def __iter__(self):
        self.current_iterator = self.head
        return self

    def __next__(self):
        while self.current_iterator is not None:
            item = self.current_iterator.get_data()
            self.current_iterator = self.current_iterator.get_next()
            return item
        raise StopIteration
