print('Задание 3. Детали\n')

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
products_count = 0
summ = 0
product = input('Название детали: ')

for index in range(len(shop)):
    if shop[index][0] == product:
        products_count += 1
        summ += shop[index][1]

print(f'Количество деталей: {products_count}')
print(f'Общая стоимость: {summ}')