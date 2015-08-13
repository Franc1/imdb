import urllib
import json


class Movie(object):
    """docstring for Imdb"""
    def __init__(self, title=None, id=None):
        super(Movie, self).__init__()
        if id:
            return self.get_movie_by_id(id)
        self.get_movie_json(title)

    def get_movie_json(self, title):
        url = "http://www.omdbapi.com/?t={}".format(title)
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        self._title = jsonvalues["Title"]
        self._rating = jsonvalues["imdbRating"]
        self._genre = jsonvalues["Genre"]
        self._year = jsonvalues["Year"]
        self._actors = jsonvalues["Actors"]
        self._runtime = jsonvalues["Runtime"]
        self._awards = jsonvalues["Awards"]
        self._writer = jsonvalues["Writer"]
        self._director = jsonvalues["Director"]
        self._poster_link = jsonvalues["Poster"]

    def get_movie_by_id(self, movie_id):
        url = "http://www.omdbapi.com/?i={}".format(movie_id)
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        self._title = jsonvalues["Title"]
        self._rating = jsonvalues["imdbRating"]
        self._genre = jsonvalues["Genre"]
        self._year = jsonvalues["Year"]
        self._actors = jsonvalues["Actors"]
        self._runtime = jsonvalues["Runtime"]
        self._awards = jsonvalues["Awards"]
        self._writer = jsonvalues["Writer"]
        self._director = jsonvalues["Director"]
        self._poster_link = jsonvalues["Poster"]

    def title(self):
        return self._title

    def poster(self):
        return self._poster_link

    def writer(self):
        return self._writer.split(",")

    def awards(self):
        return self._awards.split(",")

    def actors(self):
        return self._actors.split(",")

    def rating(self):
        return self._rating

    def genre(self):
        return self._genre.split(",")

    def year(self):
        return self._year

    def runtime(self):
        return self._runtime

    def director(self):
        return self._director.split(",")

    def __call__(self):
        return self.__dict__
