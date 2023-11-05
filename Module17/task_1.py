from functools import reduce
from typing import List

print('Задача 1. Новые списки\n')

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_res = list(map(lambda num: round(num ** 3, 3), floats))
names_res = list(filter(lambda name: len(name) >= 5, names))
numbers_res = reduce(lambda prev_num, cur_num: prev_num * cur_num, numbers)

print(floats_res)
print(names_res)
print(numbers_res)