from typing import List

print('Задача 2. И снова zip\n')

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda let, num: (let, num), letters, numbers))

print(result)
