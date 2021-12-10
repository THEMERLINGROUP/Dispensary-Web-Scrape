from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.sswlv.com/')
print(BeautifulSoup)
print(html_text)
loyalty_rewards = [{'Points':1, 'Reward':'$1'}, {'Points':100, 'Reward':'1 Remedy preroll'},
{'Points':200, 'Reward':'1 Silver Shelf Remedy G'}, {'Points':400, 'Reward':'SkyResin 0.5G'},
{'Points':475, 'Reward':'1 Silver Shelf Remedy 1/8'}, {'Points':500, 'Reward':'100mg Edible or JBO'},
{'Points':650, 'Reward':'0.5G Cured Remedy Vape Cartridge'}, {'Points':675, 'Reward':'1 Gold Shelf Remedy 1/8'}, {'Points':900, 'Reward':'1 Remedy Platinum 1/8'}]
Silver_Sage_Points_Program = groupby(loyalty_rewards, key=lambda x:x['Points'])
for key, value in Silver_Sage_Points_Program:
    print(key, list(value))
