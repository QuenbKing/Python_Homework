print('Задание 5. Разворот\n')

my_str = input('Введите строку: ')
res = my_str[my_str.rindex('h') - 1:my_str.index('h'):-1]
print(f'Развёрнутая последовательность между первым и последним h: {res}')