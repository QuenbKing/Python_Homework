from collections import Counter

print('Задача 3. Палиндром: возвращение\n')


def can_be_poly(line: str) -> bool:
    return len(list(filter(lambda count: count % 2 != 0, Counter(line).values()))) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
