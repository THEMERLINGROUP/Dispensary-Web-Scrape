from bs4 import BeautifulSoup
import requests
from itertools import groupby
print(BeautifulSoup)
html_text = requests.get('https://lakelifefarms.com/#home')
print(html_text)
onDutchie = True
rewards  = [{'Points':0, 'Reward':0}, {'Points':125, 'Reward':'$5 OFF Next Purchase'}, {'Points':250, 'Reward':'$10 OFF Next Purchase'}, {'Points':500, 'Reward':'$20 OFF Next Purchase'}, {'Points':750, 'Reward':'$30 OFF Next Purchase'}, {'Points':1000, 'Reward':'$40 OFF Next Purchase'}]
lake_life_rewards = groupby(rewards, key=lambda x:x['Reward'])
for key, value in lake_life_rewards:
    print(key, list(value))
links = ['https://www.linkedin.com/search/results/all/?keywords=lake%20life%20farms&origin=RICH_QUERY_SUGGESTION&position=0&searchId=2f11a74d-b9af-45ba-b45a-3f0ffd2b954e',
         'https://www.linkedin.com/in/kotlerdavid/']
staff = [{'Name':'David Kotler', 'Role':'CEO'}]
