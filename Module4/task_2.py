print('Задание 2. Генерация\n')

answer = [(1 if num % 2 == 0 else num % 5) for num in range(int(input('Введите длину списка: ')))]
print(answer)