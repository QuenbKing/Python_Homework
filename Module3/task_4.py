print('Задание 4. Вечеринка\n')

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
max_guests_count = 6

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}\n')
    print("Если хотите завершить работу программу введите 'Пора спать' ")
    answer = input('Гость пришёл или ушёл? ')

    if answer == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) == max_guests_count:
            print(f'Прости, {name}, но мест нет.\n')
        else:
            print(f'Привет! {name}!\n')
            guests.append(name)
    elif answer == 'ушёл':
        name = input('Имя гостя: ')
        print(f'Пока, {name}!\n')
        guests.remove(name)
    elif answer == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
