from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://ozcannabis.com/')
print(BeautifulSoup)
print(html_text)
links = ['https://mywallet.deals/?m=zf4wwbfprubuewgh/#/rewards',
         'https://www.linkedin.com/in/rramstad/',
         'https://www.linkedin.com/company/oz.-recreational-cannabis/about/',
         'https://www.linkedin.com/in/derrick-gergis-01747514b/',
         'https://www.linkedin.com/in/cheyannejorgensen/'
         ]
rewards = [{'Points':0, 'Reward':0},
        {'Points':250, 'Reward':'Penny pre-roll w/purchase, penny 100mg Q Gummy with purchase, $5 OFF Purchase[$20+]'},
        {'Points':500, 'Reward':'3 pre-rolls for penny[w/purchase $30+], $15 OFF $35+ Purchase, $10 OFF 1/8 Flower'},
        {'Points':750, 'Reward':'$35 OFF $225 Ounce, 20% OFF non-sale item, $25 in-store Credit'}
        ]
Oz_Rewards = groupby(rewards, key=lambda s:s['Points'])
for key, value in Oz_Rewards:
    print(key, list(value))
staff =[{'Name':'Bob Ramstad', 'Role':'President'}, {'Name':'Derrick Gergis', 'Role':'Chief Operating Officer'}, {'Name':'Cheyanne Jorgensen', 'Role':'Director of Inventory'}, {'Name':'Hayley Tomich', 'Role':'Director of Compliance'}]
Oz_staff = groupby(staff, key= lambda x:x['Role'])
for key, value in Oz_staff:
    print(key, list(value))
onDutchie = True

