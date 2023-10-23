import zipfile

print('Задача 6. «Война и мир»\n')

file_zip = zipfile.ZipFile('voina-i-mir.zip', 'r')
file_text = file_zip.read('voina-i-mir.txt').decode("UTF-8")
file_zip.close()

letters = dict(sorted([(sym, file_text.count(sym)) for sym in file_text if sym.isalpha()], key=lambda el: -el[1]))

answer_file = open('answer.txt', 'w', encoding="UTF-8")
for key, value in letters.items():
    answer_file.write(f'{key}:{value}\n')
answer_file.close()
