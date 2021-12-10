from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://wallflower-house.com/')
BeautifulSoup
print(html_text)
points = [{'Points':50, 'Reward':'Merch TierI'}, {'Points':250, 'Reward':'Preroll'}, {'Points':300, 'Reward':'Merch TierII'}, {'Points':400, 'Reward':'1G Flower'}, {'Points':500, 'Reward':'Infused Preroll'}, {'Points':'600', 'Reward':'Edible'}, {'Points':800, 'Reward':'Merch TierIII'}, {'Points':850, 'Reward':'0.5 Cartridge'}, {'Points':1000, 'Reward':'0.5G Wax'}, {'Points':1200, 'Reward':'3.5G Flower'}, {'Points':1850, 'Reward':'1G Wax'}, {'Points':2250, 'Reward':'7G Flower'}, {'Points':4000, 'Reward':'14G Flower'}, {'Points':7000, 'Reward':'1 Ounce'}]
wallflower_points = groupby(points, key=lambda x:x['Points'])
for key, value in wallflower_points:
    print(key, list(value))

