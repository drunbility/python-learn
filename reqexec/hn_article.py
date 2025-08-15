import requests
import json


url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

r=requests.get(url)

print(f"ststus_code : {r.status_code}")

resj=r.json()

restr=json.dumps(resj,indent=4)
print(restr)

