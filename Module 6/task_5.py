print('Задание 5. Словарь синонимов\n')

pairs_count = int(input('Введите количество пар слов: '))
pairs_dict = {}

for pair_num in range(pairs_count):
    pair = input(f'{pair_num + 1}-я пара: ').lower()
    first_word, second_word = pair.split(' - ') # пробел - пробел
    pairs_dict[first_word] = second_word
    pairs_dict[second_word] = first_word

while True:
    user_word = input('Введите слово: ').lower()
    if user_word in pairs_dict:
        print(f'Синоним: {pairs_dict[user_word]}')
        break
    else:
        print('Такого слова в словаре нет.')
