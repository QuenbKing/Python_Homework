import string

print('Задача 5. Частотный анализ\n')

alphabet = list(string.ascii_lowercase)
text_file = open('text.txt', 'r', encoding='UTF-8')
lowercase_file = text_file.read().lower()
letters = dict([(sym, lowercase_file.count(sym)) for sym in lowercase_file if sym in alphabet])
text_file.close()

text_len = sum(letters[key] for key in letters.keys())
res_file = open('analysis.txt', 'w', encoding='UTF-8')
letters = dict(sorted([(letter, letters[letter]) for letter in letters.keys()],
                      key=lambda element: (-element[1], element[0])))

for key, value in letters.items():
    res_file.write(f'{key} {round(letters[key] / text_len, 3)}\n')
res_file.close()
