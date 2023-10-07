print('Задание 5. Контейнеры\n')


def print_index():
    for index in range(len(containers)):
        if containers[index] < new_container_weight:
            print(f'Номер, который получит новый контейнер: {index + 1}')
            break


containers_count = int(input('Количество контейнеров: '))
containers = []

for container in range(containers_count):
    container_weight = int(input('Введите вес контейнера: '))
    containers.append(container_weight)

new_container_weight = int(input('Введите вес нового контейнера: '))

if containers[len(containers) - 1] > new_container_weight:
    print(f'Номер, который получит новый контейнер: {len(containers) + 1}')
else:
    print_index()
