from bs4 import BeautifulSoup
from bs4.element import PreformattedString
import requests
from itertools import groupby
html_text = requests.get('https://whitemountainhealthcenter.com/')
print(BeautifulSoup)
print(html_text)
onDutchie = False
rewards = [{'Points':0, 'Rewards':0}, {'Points':400, 'Rewards':'$50 in-house credit'}]
White_Mountain_Rewards = groupby(rewards, key=lambda x:x['Rewards'])
for key, value in White_Mountain_Rewards:
    print(key, list(value))
links = ['https://www.linkedin.com/in/scott-hoy-3a9727122?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB5dB3EBWFzzlVt-TZAVShL5Ym1GNQRs2QM&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BxRT6LYOVRtqs9oeelK%2Bxvw%3D%3D',
'']
staff = [{'Name': 'Scott Hoy', 'Role': 'Digital Marketing Designer'}, {'Name': 'Daryl "Butch" Williams', 'Role':'Owner'}]
White_Mountain_Staff = groupby(staff, key=lambda s:s['Role'])
for key, value in White_Mountain_Staff:
    print(key, list(value))


