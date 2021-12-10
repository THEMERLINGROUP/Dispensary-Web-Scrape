from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://goembarc.com/')
print(BeautifulSoup)
print(html_text)
points = [{'Points':0, 'Reward':0}, {'Points':100, 'Reward':'$5 OFF purchase'}, {'Points':300, 'Reward':'$15 OFF purchase'}, {'Points':500, 'Reward':'$25 OFF purchase'}, {'Points':1000, 'Reward':'$50 OFF purchase'}, {'Points':1500, 'Reward':'$75 OFF Purchase'}]
passport_points = groupby(points, key=lambda x:x['Reward'])
for key, value in passport_points:
    print(key, list(value))
onDutchie = True


