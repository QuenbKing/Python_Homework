class Stack:
    def __init__(self):
        self.__stack_list = []

    def get_list(self):
        return self.__stack_list

    def is_empty(self):
        return len(self.__stack_list) == 0

    def put(self, item):
        self.__stack_list.append(item)

    def get(self):
        if not self.__stack_list:
            return None
        return self.__stack_list.pop()

    def remove(self, item):
        self.__stack_list.remove(item)

    def __str__(self):
        return str(self.__stack_list)
