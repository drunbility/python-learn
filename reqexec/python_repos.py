import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"

url+="?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}

r= requests.get(url,headers=headers)

print(f"status code {r.status_code}")


response_j = r.json()


print(response_j.keys())

print(f"total count :{response_j['total_count']}")

print(f"complete result: {not response_j['incomplete_results']}")

repo_dicts = response_j['items']

print(f"return repos:{len(repo_dicts)}")

repo_dic = repo_dicts[0]

print(f"\nKeys:{len(repo_dic)}")

#for ky in sorted(repo_dic.keys()):
#    print(ky)
#
names,stars,hovers,links = [],[],[],[]



print(f"\nSelect information each repo:")

for rep in repo_dicts:
    print(f"\nName: {rep['name']}")
    names.append(rep['name'])
    print(f"Owner: {rep['owner']['login']}")
    print(f"Stars: {rep['stargazers_count']}")
    stars.append(rep['stargazers_count'])
    print(f"Url: {rep['html_url']}")
    hovers.append(rep['description'])

    repo_link=f"<a href='{rep['html_url']}'>{rep['name']}</a>"
    links.append(repo_link)

title = "most stars on github"

labels = {'x':"repos",'y':"stars"}


fig = px.bar(x=links,y=stars,title=title,labels=labels,hover_name=hovers)
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)
fig.show()
