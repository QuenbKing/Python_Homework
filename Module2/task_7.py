print('Задание 7. Анализ слова — 2\n')

text = input('Ввдеите слово: ') * 100000

symbols = list(text)

for sym_index in range(len(symbols)):
    if symbols[sym_index] != symbols[len(symbols) - 1 - sym_index]:
        print('Слово не является палиндромом')
        break
else:
    print('Слово является палиндромом')

'''Без списка вариант

text = input('Введите строку: ').lower().translate(str.maketrans('', '', '!.?,'))

if text == text[::-1]:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром')'''