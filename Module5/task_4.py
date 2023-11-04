print('Задание 4. Заглавные буквы\n')

text = input('Введите строку: ').split()

for index in range(len(text)):
    text[index] = text[index].replace(text[index][0], text[index][0].upper())

print(f"Результат: {' '.join(text)}")

# text = input('Введите строку: ')
# print(text.title())


