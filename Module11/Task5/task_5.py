from home import Home
from human import Human

print('Задача 5. Совместное проживание\n')

home = Home()
human_1 = Human('Артём', home)
human_2 = Human('Николай', home)
day = 1

while human_1.satiety >= 0 and human_2.satiety >= 0 and day <= 365:
    print(f'День {day}')
    human_1.live_the_day()
    human_2.live_the_day()
    human_1.print_info()
    human_2.print_info()
    home.print_info()
    day += 1
