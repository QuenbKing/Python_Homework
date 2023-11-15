from Property import Apartment, Car, CountryHouse

print('Задача 1. Налоги\n')

cash = int(input('Введите количество денег: '))
user_property = int(input('Что хотите купить? (1.Апартамены, 2.Машину, 3.Дачу): '))
worth = int(input('Стоимость собственности: '))

try:
    if user_property == 1:
        your_property = Apartment(worth)
    elif user_property == 2:
        your_property = Car(worth)
    elif user_property == 3:
        your_property = CountryHouse(worth)
    else:
        raise ValueError()
    tax = your_property.get_tax()
    print(f'Налог составляет {tax} рублей')
    if cash < tax:
        print(f'Для выплаты налога вам не хватает {tax - cash} рублей')
except ValueError:
    print('Введён неверный номер собственности')
