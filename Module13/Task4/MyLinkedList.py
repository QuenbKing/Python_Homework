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
        self.__count = 0
        self.__head = None
        self.__tail = None
        self.__current_iterator = self.__head

    def append(self, value):
        node = Node(value)
        if self.__count == 0:
            self.__head = self.__tail = node
        else:
            self.__tail.set_next(node)
            self.__tail = node
        self.__count += 1

    def get(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError

        cur_node = self.__head
        for _ in range(index):
            cur_node = cur_node.get_next()
        return cur_node.get_data()

    def remove(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError

        if index == 0:
            self.__head = self.__head.get_next()
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.get_next()
            current.set_next(current.get_next().get_next())
            if index == self.__count - 1:
                self.__tail = current
        self.__count -= 1

    def __str__(self):
        return f"[{', '.join(str(el) for el in self)}]"

    def __iter__(self):
        self.__current_iterator = self.__head
        return self

    def __next__(self):
        while self.__current_iterator is not None:
            item = self.__current_iterator.get_data()
            self.__current_iterator = self.__current_iterator.get_next()
            return item
        raise StopIteration
