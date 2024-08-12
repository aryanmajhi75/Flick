import requests

def showData(list):
    # print(list)
    for i in list:
        print("-" * 20)
        print(f"Movie ID          :: {i['id']}")
        print("-" * 20)
        print(f"Movie name        :: {i['title']}")
        print(f"Release Year      :: {i['year']}")
        print(f"Description       :: {i['type']}")
        print("-" * 20)
        print("\n")

def getAMovie():
  url = "https://mdblist.p.rapidapi.com/"

  querystring = {"s":"jaws","m":"movie"}

  headers = {
    "x-rapidapi-key": "510e846ffemsh1b33d4dacf50dc7p17cd4ejsn971e84540326",
    "x-rapidapi-host": "mdblist.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  movies_data = []

  print(response.json())

  if response.status_code==200:
    data = response.json()

    # data_list = data.get("data", [])

    for show in data:
      movie_data = {
        "id": show.get('id'),
        "title": show.get('title'),
        "year": show.get('year'),
        "type": show.get('type'),
      }
      movies_data.append(movie_data)
    print("Mathces : \n")
    showData(movie_data)