import requests

def showData(list):
  for i in list:
       print("-"*20)
       print(i['id'])
       print("-"*20)
       print(f"Show name        :: ${i['name']}")
       print(f"Year of Release  :: ${i['year']}")
       print("-"*20)
       print("\n")

  return list
# def getShows():
url = "https://movies-tv-shows-database.p.rapidapi.com/"

querystring = {"year":"2023","page":"1"}

headers = {
    "x-rapidapi-key": "510e846ffemsh1b33d4dacf50dc7p17cd4ejsn971e84540326",
    "x-rapidapi-host": "movies-tv-shows-database.p.rapidapi.com",
    "Type": "get-shows-byyear"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

shows_data=[]

if response.status_code==200:
  data_list=response.json()

  data=data_list.get("data", [])

  for show in data:
    show_data = {
                      "id": show.get('imdb_id'),
                      "name": show.get('title'),
                      "year": show.get('year'),
                  }
    shows_data.append(show_data)

  showData(shows_data)

else:
    print("Oops! Ran into some error T_T")

# if __name__ == 'main':
#     getShows()