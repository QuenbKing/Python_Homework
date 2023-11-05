from collections import Counter

print('Задача 4. Уникальный шифр\n')


def count_unique_characters(text: str) -> int:
    return len(list(filter(lambda count: count == 1, Counter(text.lower()).values())))


message = input('Введите текст: ')
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
