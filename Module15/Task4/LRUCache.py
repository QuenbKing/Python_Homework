from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = OrderedDict()

    def print_cache(self):
        print(self.__class__.__name__)
        for key, value in self.__cache.items():
            print(f"{key} : {value}")

    def get(self, key):
        value = self.__cache.pop(key)
        self.__cache[key] = value
        return value

    @property
    def cache(self):
        if self.__cache:
            key, value = list(self.__cache.items())[0]
            return f"{key} : {value}"
        else:
            return "Cache is empty"

    @cache.setter
    def cache(self, new_elem):
        if new_elem[0] in self.__cache:
            del self.__cache[new_elem[0]]
        elif len(self.__cache) == self.__capacity:
            self.__cache.popitem(last=False)
        self.__cache[new_elem[0]] = new_elem[1]
