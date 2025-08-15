from operator import itemgetter
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

res = requests.get(url)

print(f"status code : {res.status_code}")

sub_ids = res.json()
sub_dicts = []
for id in sub_ids[:5]:
    url=f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    r= requests.get(url)
    r_d = r.json()

    sub_dic = {
        'title':r_d['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={id}",
        'comments':r_d['descendants'],
    }

    sub_dicts.append(sub_dic)

sub_dicts = sorted(sub_dicts,key=itemgetter('comments'),reverse=True)

for sb in sub_dicts:
    print(f"\ntitle: {sb['title']}")
    print(f"discussion_link:{sb['hn_link']}")
    print(f"comments:{sb['comments']}")
