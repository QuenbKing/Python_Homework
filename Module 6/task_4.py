print('Задание 4. Гистограмма частоты — 2\n')

text = input('Введите текст: ')
original_dict = {}

for sym in text:
    if sym in original_dict:
        original_dict[sym] += 1
    else:
        original_dict[sym] = 1

print('Оригинальный словарь частот: ')
for key in sorted(original_dict.keys()):
    print(f'{key}: {original_dict[key]}')

inverted_dict = {}
for letter, count in original_dict.items():
    if count in inverted_dict:
        inverted_dict[count].append(letter)
    else:
        inverted_dict[count] = list(letter)

print('Инвертированный словарь частот: ')
for key in sorted(inverted_dict.keys()):
    print(f'{key}: {inverted_dict[key]}')