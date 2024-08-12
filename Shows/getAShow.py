import requests

def showData(list):
    # print(list)
    for i in list:
        print("-"*20)
        print(i['id'])
        print("-"*20)
        print(f"Show name        :: ${i['title']}")
        print(f"Year of Release  :: ${i['year']}")
        print("-"*20)
        print("\n")

def getAShow():
  url = "https://mdblist.p.rapidapi.com/"

  querystring = {"s":"friends","m":"show"}

  headers = {
    "x-rapidapi-key": "510e846ffemsh1b33d4dacf50dc7p17cd4ejsn971e84540326",
    "x-rapidapi-host": "mdblist.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  shows_data = []

  print(response.json())

  if response.status_code==200:
    data = response.json()

    # data_list = data.get("data", [])

    for show in data:
      show_data = {
        "id": show.get('id'),
        "title": show.get('title'),
        "year": show.get('year'),
      }
      shows_data.append(show_data)
    print("Matches : \n")
    showData(show_data)