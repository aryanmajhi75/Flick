import requests
import string

def showData(list):
    # print(list)
    for i in list:
        print("-" * 20)
        print(f"Movie ID          :: {i['id']}")
        print("-" * 20)
        print(f"Movie name        :: {i['name']}")
        print(f"Genre(s)          :: {i['genre']}")
        print(f"Release Year      :: {i['year']}")
        print(f"Movie Rating      :: {i['rating']}")
        print(f"Certificate       :: {i['cert']}")
        print(f"Runtime           :: {i['runtime']}")
        print(f"Director          :: {i['director']}")
        print(f"Stars             :: {i['stars']}")
        print(f"Description       :: {i['desc']}")
        print("-" * 20)
        print("\n")

# def getMovie():
url = "https://random-chunk-api.p.rapidapi.com/api/movie"

querystring = {"count":"10"}

headers = {
        "x-rapidapi-key": "510e846ffemsh1b33d4dacf50dc7p17cd4ejsn971e84540326",
        "x-rapidapi-host": "random-chunk-api.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
movies_data=[]

if response.status_code==200:
        data=response.json()

        if data.get("success"):
            data_list = data.get("data", [])

            for movie in data_list:
                movie_data = {
                        "id": movie.get('id'),
                        "name": movie.get('name'),
                        "year": movie.get('year'),
                        "cert": movie.get('cert'),
                        "runtime": movie.get('runtime'),
                        "genre": movie.get('genre'),
                        "rating": movie.get('rating'),
                        "desc": movie.get('desc'),
                        "director": movie.get('director'),
                        "stars": movie.get('stars')
                    }
                movies_data.append(movie_data)

            showData(movies_data)

else:
        print("Oops! Ran into some error T_T")
