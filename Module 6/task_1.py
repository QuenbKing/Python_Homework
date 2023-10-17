print('Задание 1. Песни — 2\n')

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_count = int(input('Сколько песен выбрать? '))
songs_duration = 0

for song_num in range(songs_count):
    song_title = input(f'Название {song_num + 1} - й песни: ')
    songs_duration += violator_songs.get(song_title)

print(f'Общее время звучания песен: {round(songs_duration, 2)} минуты')