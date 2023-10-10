print('Задание 1. Гласные буквы\n')

text = input('Введите текст: ').lower()
vowel_letters = [let for let in text if let in ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'ю', 'и', 'е']]
print(f'Список гласных букв: {vowel_letters}')
print(f'Длина списка: {len(vowel_letters)}')