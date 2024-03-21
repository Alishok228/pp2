def imdb_above_5_5(movie):
    return movie['imdb'] > 5.5

def movies_above_5_5(movie_list):
    return [movie for movie in movie_list if imdb_above_5_5(movie)]

def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie['category'] == category]

def average_imdb_score(movie_list):
    if not movie_list:
        return 0
    total_score = sum(movie['imdb'] for movie in movie_list)
    return total_score / len(movie_list)

def average_imdb_score_by_category(movie_list, category):
    category_movies = movies_by_category(movie_list, category)
    return average_imdb_score(category_movies)

# Пример использования функций:
print(imdb_above_5_5(movies[0]))
print(movies_above_5_5(movies))
print(movies_by_category(movies, 'Romance'))
print(average_imdb_score(movies))
print(average_imdb_score_by_category(movies, 'Romance'))
