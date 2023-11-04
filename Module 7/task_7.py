print('Задача 7. Своя функция zip\n')

text = input('Строка: ')
my_tuple = tuple(int(input('Введите число: ')) for _ in range(len(text)))
print(f'Кортеж: {my_tuple}')
generator = ((text[i], my_tuple[i]) for i in range(len(text)))
print(generator)
for el in generator:
    print(el)
