print('Задача 6. Контакты — 3\n')

contacts = {}

while True:
    find_person = False
    action_number = int(input('Введите номер действия: (1.Добавить контакт, 2.Найти человека.): '))
    if action_number == 1:
        person = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if person in contacts:
            print('Такой человек уже есть в контактах.')
        else:
            tel_num = int(input('Введите номер телефона: '))
            contacts[person] = tel_num
    elif action_number == 2:
        surname = input('Введите фамилию: ')
        for person, tel_num in contacts.items():
            if surname in person:
                print(' '.join(person), tel_num)
                find_person = True
        if not find_person:
            print('Такого контакта нет!')
    print(f'Текущий словарь контактов: {contacts}')


