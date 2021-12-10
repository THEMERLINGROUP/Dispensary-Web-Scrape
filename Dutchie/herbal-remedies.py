from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://herbalremediesil.com/')
print(html_text, BeautifulSoup)
online_store = True
rewards_online = True
Discounts = [('Medical Patient Discounts'), ('Vet Discount'), ('SAME-DAY Disount- take receipt to another store for 5%OFF')]
Best_Budzz = [{'Points':0, 'Rewards':0}, {'Points':750, 'Rewards':'$20 OFF Cannabis'}, {'Points':1500, 'Rewards':'$50 OFF Cannabis'}, {'Points':3000, 'Rewards':'$120 OFF Cannabis'}]
Rewards = groupby(Best_Budzz, key= lambda x:x['Rewards'])
for key, value in Rewards:
    print(key, list(value))
Links = ['https://www.linkedin.com/in/christine-wildrick-745b56128/',
         'https://herbalremediesil.com/bestbudzz/']
Staff = [{'Name':'Christine Wildrick', 'Role':'Chief Operating Officer'}, {'Name':'Bob Lansing', 'Role':'CEO'}]
Herbal_Remedies_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in Herbal_Remedies_Staff:
    print(key, list(value))
onDutchie = True

