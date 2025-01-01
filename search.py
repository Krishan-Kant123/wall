import requests
import json

def search(st:str):
   url = "https://wallpaper.mob.org/xrequest/search/"

   payload = {
    "razdel": "pic",
    "search_word": st,
    "offset": 0,
    "limit": 15,
    "pc": ""
   }

   headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
   }

   response = requests.post(url, data=payload, headers=headers)

   if response.status_code == 200:
    data = response.json()
    return json.dumps(data, indent=4, sort_keys=True)
   else:
     return "no results"
    