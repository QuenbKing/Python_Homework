print('Задание 8. Снова палиндром\n')

text = input('Введите строку: ').lower().translate(str.maketrans('', '', '.,!?:; '))
chars_count = {}

for sym in text:
    if sym in chars_count:
        chars_count[sym] += 1
    else:
        chars_count[sym] = 1

odd_num = 0
for count in chars_count.values():
    if count % 2 != 0:
        odd_num += 1

if odd_num <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')