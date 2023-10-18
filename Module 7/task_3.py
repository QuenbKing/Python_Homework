print('Задача 3. Игроки\n')

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_stats = [person + scores for person, scores in players.items()]
print(players_stats)