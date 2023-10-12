print('Задание 9. Анализ комментариев\n')


def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0
    for sym in text:
        if sym.isupper():
            uppercase += 1
        elif sym.islower():
            lowercase += 1
    return lowercase, uppercase


text = input('Введите строку для анализа: ')
lowercase, uppercase = count_uppercase_lowercase(text)
print(f'Количество заглавных букв: {uppercase}')
print(f'Количество строчных букв: {lowercase}')
