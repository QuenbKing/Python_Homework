print('Задание 6. Пицца\n')

orders_count = int(input('Введите количество заказов: '))
my_dict = {}

for order_num in range(orders_count):
    order = input(f'{order_num + 1} - й заказ: ')
    name, pizza, count = order.split()
    if name in my_dict and pizza in my_dict[name]:
        my_dict[name][pizza] += int(count)
    elif name not in my_dict:
        my_dict[name] = {pizza: int(count)}
    else:
        my_dict[name][pizza] = int(count)

for key in sorted(my_dict.keys()):
    print(f'{key}:')
    for pizza_keys in sorted(my_dict[key].keys()):
        print(f'{pizza_keys}: {my_dict[key][pizza_keys]}')