from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.wintergreensdelivery.com/order?')
usesPayTender = True
points = [{'Points':0, 'Value':0}, {'Points':200, 'Value':'$1 0.5 preroll'}, {'Points':250, 'Value':'$10 OFF 1G of flower'}, {'Points':300, 'Value':'$15 OFF cartridge/concentrate purchase'}, {'Points':325, 'Value':'$15 OFF any 20 pack of FruitChew/Lozenge'}, {'Points':500, 'Value':'$35 OFF 1/8 of Flower'}, {'Points':550, 'Value':'40% OFF Topical/Tincture/Capsule'}, {'Points':600, 'Value':'$45 OFF 7G Flower'}, {'Points':650, 'Value':'50% OFF any edible'}]
Loyalty_points = groupby(points, key=lambda x:x['Points'])
for key, value in Loyalty_points:
    print(key, list(value))
