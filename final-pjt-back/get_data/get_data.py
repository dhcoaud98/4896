import urllib.request
import json
import requests


# api_key와 url
TMDB_API_KEY = '11fca68c2a4afa584e0c7704a48f54d3'

HOST = 'http://api.themoviedb.org'
MOVIE_POPULAR_URL = '/3/movie/popular'
MOVIE_LIST_URL = '/3/movie/'
GENRE_LIST_URL = '/3/genre/movie/list'


movie_list = []
movie_Ids = []
genre_list = []

def get_movie_datas():
    

    # genre 데이터
    genre_request = (f'{HOST}{GENRE_LIST_URL}?api_key={TMDB_API_KEY}&language=ko')
    json_object = requests.get(genre_request).json()

    genre_data = json_object.get("genres")

    for data in genre_data:

        my_data = {
            "number": data.get("id"),
            "name": data.get("name")
        }

        my_genre = {
            "model": "movies.genre",
            "pk": my_data.get("number"),
            "fields": {
                "name": my_data.get("name")
            },
        }
        genre_list.append(my_genre)
        

    # movie popular 데이터
    for i in range(1, 6):
        request_url = (f'{HOST}{MOVIE_POPULAR_URL}?api_key={TMDB_API_KEY}&language=ko&page={i}')
        data_movies = requests.get(request_url).json()
        # print(data_movies)
        movies = data_movies.get('results')
        # print(movies)
        for movie in movies:
            movie_Ids.append(movie.get("id"))
    # print(movie_Ids)
    for idx, movie_Id in enumerate(movie_Ids):        
        movie_request = (f'{HOST}{MOVIE_LIST_URL}{movie_Id}?api_key={TMDB_API_KEY}&language=ko&')
        response = urllib.request.urlopen(movie_request)
        json_str = response.read().decode('utf-8')
        json_object = json.loads(json_str)
        if json_object.get('poster_path'):
            if json_object.get('genres'):
                    
                my_object = {
                    "model": "movies.movie",
                    "pk": idx+1,
                    "fields": {
                        "title": json_object.get("title"),
                        "overview": json_object.get("overview"),
                        "poster_path": json_object.get("poster_path"),
                        "vote_average": json_object.get("vote_average"),
                        "release_date": json_object.get("release_date"),
                        "runtime": json_object.get("runtime"),
                        "popularity": json_object.get("popularity"),
                        "genre": [json_object.get("genres")[0].get("id")],
                        "adult": json_object.get("adult"),
                    }  
                }
            else:
                my_object = {
                    "model": "movies.movie",
                    "pk": idx+1,
                    "fields": {
                        "title": json_object.get("title"),
                        "overview": json_object.get("overview"),
                        "poster_path": json_object.get("poster_path"),
                        "vote_average": json_object.get("vote_average"),
                        "release_date": json_object.get("release_date"),
                        "runtime": json_object.get("runtime"),
                        "popularity": json_object.get("popularity"),
                        "genre": json_object.get("genre"),
                        "adult": json_object.get("adult"),
                    }  
                }
            movie_list.append(my_object)
    # print(movie_list)

    with open('movies.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(movie_list, indent=4, ensure_ascii=False))

    with open('genres.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(genre_list, indent=4, ensure_ascii=False))



get_movie_datas()
