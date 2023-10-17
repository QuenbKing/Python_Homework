print('Задание 3. Товары\n')


def getCountAndPrice(goods_dict, store_dict, name, quantity_key, price_key):
    types_count = len(store_dict[goods_dict[name]])
    count = 0
    price = 0
    for num in range(types_count):
        count += store_dict[goods_dict[name]][num][quantity_key]
        price += store_dict[goods_dict[name]][num][quantity_key] * store_dict[goods_dict[name]][num][price_key]
    return count, price


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamps_count, lamps_price = getCountAndPrice(goods, store, 'Лампа', 'quantity', 'price')
tables_count, tables_price = getCountAndPrice(goods, store, 'Стол', 'quantity', 'price')
sofas_count, sofas_price = getCountAndPrice(goods, store, 'Диван', 'quantity', 'price')
chairs_count, chairs_price = getCountAndPrice(goods, store, 'Стул', 'quantity', 'price')

print(f'Лампа — {lamps_count} штук, стоимость {lamps_price} рубля.')
print(f'Стол — {tables_count} штуки, стоимость {tables_price} рублей.')
print(f'Диван — {sofas_count} штуки, стоимость {sofas_price} рублей.')
print(f'Стул — {chairs_count} штук, стоимость {chairs_price} рублей')
