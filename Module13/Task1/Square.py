class Square:
    def __init__(self, count):
        self.__start_num = 0
        self.__count = count

    def __iter__(self):
        self.__start_num = 0
        return self

    def __next__(self):
        while self.__start_num < self.__count:
            self.__start_num += 1
            return self.__start_num ** 2
        raise StopIteration
