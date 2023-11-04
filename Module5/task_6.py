print('Задание 6. Сжатие\n')

text = input('Введите строку: ')
encoded_text = ''
count = 1
for index in range(1, len(text) + 1):
    if index == len(text) or text[index] != text[index - 1]:
        encoded_text = ''.join([encoded_text, text[index - 1], str(count)])
        count = 1
    else:
        count += 1

print(encoded_text)