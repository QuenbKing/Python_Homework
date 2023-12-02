import re

print('Задача 2. Регистрационные знаки\n')

checklist = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_cars = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', checklist)
print(f'Список номеров частных автомобилей: {private_cars}')

taxi = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', checklist)
print(f'Список номеров такси: {taxi}')
