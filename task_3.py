print('Задание 3. Видеокарты\n')

videoCards_count = int(input('Введите количество видеокарт: '))
video_cards = []

for i in range(videoCards_count):
    video_card = int(input(f'Видеокарта {i + 1}: '))
    video_cards.append(video_card)

print(f'Старый список видеокарт: {video_cards}')
max_el = max(video_cards)
for card in video_cards:
    if card == max_el:
        video_cards.remove(card)
print(f'Новый список видеокарт: {video_cards}')