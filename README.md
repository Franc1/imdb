# imdb
Searches and Collects movie information with title or imdb id
##Examples:

```python
from imdb import Movie

movie = Movie(title='The Matrix')  # or 
movie = Movie(id="tt0133093")
print movie.actors()
>>>>[u'Keanu Reeves', u' Laurence Fishburne', u' Carrie-Anne Moss', u' Hugo Weaving']

print movie.genre()
>>>>[u'Action', u' Sci-Fi']

print movie.rating()
>>>>8.7

print movie.poster()
>>>>http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX300.jpg

``` 
```python
from imdb import Search

results = Search('eternal').get_list()
>>>>[{u'imdbID': u'tt0338013', u'Year': u'2004', u'Type': u'movie', u'Title': u'Eternal Sunshine of the Spotless Mind'}, {u'imdbID': u'tt0885520', u'Year': u'2006', u'Type': u'movie', u'Title': u'Eternal Summer'}, {u'imdbID': u'tt0156524', u'Year': u'1940', u'Type': u'movie', u'Title': u'The Eternal Jew'}, {u'imdbID': u'tt0158011', u'Year': u'1998', u'Type': u'movie', u'Title': u'The Eternal'}, {u'imdbID': u'tt0382019', u'Year': u'2004', u'Type': u'movie', u'Title': u'Eternal'}, {u'imdbID': u'tt2404217', u'Year': u'2013', u'Type': u'movie', u'Title': u'The Eternal Zero'}, {u'imdbID': u'tt1488591', u'Year': u'2009', u'Type': u'movie', u'Title': u'Professor Layton and the Eternal Diva'}, {u'imdbID': u'tt0287665', u'Year': u'2002', u'Type': u'movie', u'Title': u'Eternal Blood'}, {u'imdbID': u'tt3642618', u'Year': u'2015', u'Type': u'movie', u'Title': u'Life Eternal'}, {u'imdbID': u'tt0402764', u'Year': u'2004', u'Type': u'movie', u'Title': u'Love Is Eternal While It Lasts'}]

movies_with_eternal = Search('eternal').get_all() # returns a generator of Movie
for m in movies_with_eternal:
    print m.title()
    
>>>> Eternal Sunshine of the Spotless Mind
>>>> Eternal Summer
>>>> The Eternal Jew
>>>> The Eternal
>>>> Eternal
>>>> The Eternal Zero
>>>> Professor Layton and the Eternal Diva
>>>> Eternal Blood
>>>> Life Eternal
>>>> Love Is Eternal While It Lasts

``` 
