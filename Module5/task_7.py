print('Задание 7. IP-адрес 2\n')

while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        continue
    for el in ip_address:
        if not el.isdigit():
            print(f'{el} — это не целое число')
            break
        elif 255 < int(el) > 0:
            print(f'{int(el)} превышает 255.')
            break
    else:
        print('IP-адрес корректен.')
        break