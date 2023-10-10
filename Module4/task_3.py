import random

print('Задание 3. Случайные соревнования\n')

count = 20
team_1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_2 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]

winners = [max(team_1[i], team_2[i]) for i in range(count)]
print(f'Первая команда: {team_1}')
print(f'Вторая команда: {team_2}')
print(f'Победители тура: {winners}')