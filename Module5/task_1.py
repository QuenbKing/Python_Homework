print('Задание 1. Меню ресторана\n')

print('Вводите блюда через ";"')
available_menu = input('Доступное меню: ').split(';')
current_menu = ', '.join(available_menu)
print(f'Сейчас в меню есть: {current_menu}')