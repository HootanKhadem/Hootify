from difflib import SequenceMatcher

from imdb import IMDb


def get_movie(movie_name):
    ia = IMDb()
    movies_detail = ia.search_movie(movie_name)
    for single_movie in movies_detail:
        if SequenceMatcher(None, single_movie.data['title'].lower(), movie_name.lower()).ratio() > 0.7 \
                and single_movie.data['kind'] == 'movie':
            movie = ia.get_movie(single_movie.movieID)
            return movie
