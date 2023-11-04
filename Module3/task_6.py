print('Задание 6. Ролики\n')

rollers = []
people = []

rollers_count = int(input('Количество роликов: '))
people_with_rollers_cnt = 0

for roller_num in range(rollers_count):
    pair_size = int(input(f'Размер пары {roller_num + 1}: '))
    rollers.append(pair_size)
print()

people_amt = int(input('Количество людей: '))

for human_num in range(people_amt):
    foot_size = int(input(f'Размер ноги человека {human_num + 1}: '))
    people.append(foot_size)
print()

people = list(set(people))  #Без дубликатов

for size in people:
    if size in rollers:
        people_with_rollers_cnt += 1

print(f'Наибольшее количество людей, которые могут взять ролики: {people_with_rollers_cnt}')
