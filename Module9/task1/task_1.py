print('Задача 1. Сумма чисел 2\n')

num_file = open('numbers.txt', 'r', encoding='UTF-8')
summ = 0
for line in num_file:
    summ += int(line)
num_file.close()

answer_file = open('answer.txt', 'w', encoding='UTF-8')
answer_file.write(str(summ))
answer_file.close()
print(f'Сумма: {summ}. Добавлено в answer.txt ')
