print('Задание 4. Кино\n')

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
favorite_movies_count = int(input('Сколько фильмов хотите добавить? '))
my_favorite_movies = []

for _ in range(favorite_movies_count):
    movie = input('Введите название фильма: ')
    if movie in films:
        my_favorite_movies.append(movie)
    else:
        print(f'Ошибка: фильма {movie} у нас нет :(')

print('Ваш список любимых фильмов:', ', '.join(my_favorite_movies))
