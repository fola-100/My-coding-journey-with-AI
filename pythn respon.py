import requests
import plotly.express as px

url= "https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>1000"

header={"Accept": "application/vnd.github.v3+json"}
r=requests.get(url, headers=header)

print(f'Status code:{r.status_code}')

response_dict=r.json()

#print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']

repo_links, stars, hover_texts = [],[],[]

print(f"Repositories returned: {len(repo_dicts)}")

for each_repo in repo_dicts:

  stars.append(each_repo["stargazers_count"])

  owner = each_repo['owner']['login']
  repo_name = each_repo["name"]
  repo_url = each_repo['html_url']
  description = each_repo['description']

  hover_text = f"{owner}<br />{description}"
  hover_texts.append(hover_text)

  repo_link =f"<a href='{repo_url}'>{repo_name}</a>"
  repo_links.append(repo_link)

#title
title="Must started project on Github"
labels = {'x': 'Repository', 'y': 'Stars'}

fig=px.bar(x=repo_links, y=stars, title=title, labels=labels,hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,yaxis_title_font_size=20)

fig.show()







