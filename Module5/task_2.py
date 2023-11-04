print('Задание 2. Самое длинное слово\n')

text = input('Введите строку: ').replace('.', '')
words = text.split()
longest_word = max(words, key=len)
max_len = len(longest_word)
print(f'Самое длинное слово: {longest_word}')
print(f'Длина этого слова: {max_len}')
