import urllib
import json
from movie import Movie

class Search(object):
    """docstring for Search"""
    def __init__(self, search_string):
        super(Search, self).__init__()
        self.get_movies_data(search_string)

    def get_movies_data(self, search_string):
        url = "http://www.omdbapi.com/?s={}".format(search_string)
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        self.movies = jsonvalues['Search']

    def get_list(self):
        return self.movies

    def get_all(self):
        for movie in self.movies:
            yield Movie(title=movie['Title'])
