from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.myntcannabis.com/')
print(html_text)
print(BeautifulSoup)
points = [{'Points':0, 'Value':0}, {'Points':150, 'Value':'$5 Coupon'},
{'Points':250, 'Value':'Pre-roll or Small glass pipe or Vape Battery'}, {'Points':350, 'Value':'$15 Coupon or Cannapunch or Edible or Infused preRoll'},
{'Points':500, 'Value':'$20 Coupon or $30 glass piece or 0.5 Concentrate or 300mg Disposable'}, {'Points':1000, 'Value':'$50 OFF glass or 1G Kanji Wax or 0.5G Sauce cart or 1/8 Top shelf'},
{'Points':5000, 'Value':'28G Flower or Huni Badger'}]
Mynt_points = groupby(points, key=lambda x:x['Points'])
for key, value in Mynt_points:
    print(key, list(value))
venture = 'Kynd Cannabis'
Mynt_Owners = [{'Name':'Mark Pitchford', 'Role':'Co-Founder'}, {'Name':'Joanna ONeal', 'Role':'Co-Founder'}, {'Name':'Dr.Sean Devlin', 'Role':'CO-Founder'}]
staff = groupby(Mynt_Owners, key=lambda x:x['Name'])
for key, value in staff:
    print(key, list(value))
