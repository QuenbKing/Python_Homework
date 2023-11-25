from Date import Date

print('Задача 3. Дата\n')

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('10-13'))
