from bs4 import BeautifulSoup
import requests
from itertools import groupby

from requests.api import head
html_text = requests.get('https://www.heads.net/')
print(BeautifulSoup)
print(html_text)
rewards_online = True
onDutchie = True
links = ['https://www.linkedin.com/in/abe-aoun-94b38b4/',
         'https://mywallet.deals/?m=zkbkweezrubrce1h/#/rewards']
Rewards = [{'Points':0, 'Reward':0}, {'Points':50, 'Reward':'rolling papers/lighters'},
{'Points':100, 'Reward':'wraps'}, {'Points':125, 'Reward':'$5 OFF, heavyweight heads mask'},
{'Points':185, 'Reward':'$10 OFF Order'}, {'Points':200, 'Reward':'house preroll'}, {'Points':225, 'Reward':'Chillum'},
{'Points':250, 'Reward':'$15 OFF Order'}, {'Points':275, 'Reward':'1G of flower'}, {'Points':300, 'Reward':'Heads shirt, Heavyweight heads shirt'},
{'Points':350, 'Reward':'Heavyweight grinder'}, {'Points':400, 'Reward':'$25 OFF Order'}, {'Points':425, 'Reward':'VFire or MAXX Battery'},
{'Points':450, 'Reward':'Hand pipe'}, {'Points':500, 'Reward':'Hat'}, {'Points':650, 'Reward':'Screen Print Hoodie'},
{'Points':750, 'Reward':'$50 OFF Order'}, {'Points':800, 'Reward':'FREE 1/8'}, {'Points':1145, 'Reward':'$75 OFF'}, {'Points':1490, 'Reward':'$100 OFF'},
{'Points':2100, 'Reward':'Limited Edition Indica Hoodie'}, {'Points':2200, 'Reward':'$150 OFF Order'}]
head_rewards = groupby(Rewards, key=lambda s:s['Points'])
for key, value in head_rewards:
    print(key, list(value))
staff = [{'Name': 'Abe Aoun', 'Role':'GM'}]
