print('Задача 5. Песни\n')

violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56],
                  ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]]
songs_duration = 0
songs_count = int(input('Сколько песен выбрать? '))

for song_num in range(songs_count):
    song_name = input(f'Название {song_num + 1}-й песни: ')
    for song in violator_songs:
        if song[0] == song_name:
            songs_duration += song[1]
            break

print(f'Общее время звучания песен — {round(songs_duration, 2)} минуты')