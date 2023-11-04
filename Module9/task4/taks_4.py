print('Задача 4. Турнир\n')

first_tour_file = open('first_tour.txt', 'r', encoding="UTF-8")
second_tour_file = open('second_tour.txt', 'w', encoding="UTF-8")
winners = []

need_points = first_tour_file.readline()
participants = first_tour_file.readlines()

for participant in participants:
    surname, name, points = participant.split()

    if points > need_points:
        winners.append((surname, name, points))
first_tour_file.close()

winners.sort(reverse=False)

second_tour_file.write(f'{str(len(winners))}\n')
for num in range(len(winners)):
    second_tour_file.write(f'{num + 1}) {winners[num][1][0]}. {winners[num][0]}, {winners[num][2]}\n')
second_tour_file.close()


