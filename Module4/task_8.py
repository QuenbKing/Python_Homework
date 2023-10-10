print('Задание 8. Шифр Цезаря\n')

my_str = input('Введите сообщение: ')
offset = int(input('Введите сдвиг: '))
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
additional_characters = [' ', '!', '?', '.', ',']
res_str = ""

for letter in my_str:
    if letter in additional_characters:
        res_str += letter
    else:
        res_str += letters[(letters.index(letter) + offset) % len(letters)]

print(f'Зашифрованное сообщение: {res_str}')