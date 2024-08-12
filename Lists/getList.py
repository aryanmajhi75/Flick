import requests
import string

API_KEY="6ea31d7d9a760bd1016eb6a61813f8da"

def showData(list):
    # print(list)
    for i in list:
       print("-"*20)
       print(i['id'])
       print("-"*20)
       print(f"Movie name        :: ${i['title']}")
       print(f"Genre(s)          :: ${i['genre']}")
       print(f"Release Date      :: ${i['release_date']}")
       print(f"Movie Status      :: ${i['status']}")
       print(f"Original Language :: ${i['original_language']}")
       print(f"Adult?            :: ${i['adult']}")
       print("-"*20)
       print("\n")

def getData():
    url = "https://moviedatabase8.p.rapidapi.com/Search/Incep"

    headers = {
        "x-rapidapi-key": "510e846ffemsh1b33d4dacf50dc7p17cd4ejsn971e84540326",
        "x-rapidapi-host": "moviedatabase8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response)
    movies_data=[]

    if response.status_code==200:
        data_list=response.json()

        for data in data_list:
            movie_data = {
                        "id": data.get('id'),
                        "title": data.get('title'),
                        "release_date": data.get('release_date'),
                        "genre": data.get('genres'),
                        "original_language": data.get('original_language'),
                        "status": data.get('status'),
                        "adult": data.get('adult')
                    }
            movies_data.append(movie_data)

        showData(movies_data)

    else:
        print("Oops! Ran into some error T_T")

if __name__ is 'main':
    getData()