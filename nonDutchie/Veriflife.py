from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.verilife.com/')
soup = BeautifulSoup(html_text, 'lxml')
#ONLY Illinois and Massachusetts have recreational dispensaries
legal_states = ['Illinois', 'Massachusetts', 'Maryland', 'New York', 'Ohio', 'Pennsylvania']
#NO LIMIT TO REWARDS you can earn
Points_system = [{'Points': 0, 'Rewards': 0}, {'Points': 200, 'Rewards':'$5'}, {'Points':400, 'Rewards':'$10'}, {'Points':800, 'Rewards':'$20'}]
group_Points = groupby(Points_system, key=lambda x:x['Rewards'])
for key, value in group_Points:
    print(key, list(value))
Illinois_Recreational_Dispensaries = [{'Name':'Ottawa Recreational'}, {'Name': 'North Aurora Recreational'}, {'Name':'Arlington Heights Recreational'}, {'Name':'Removille Recreational'}, {'Name':'Rosemont Recreational'}, {'Name':'Galena Recreational'}, {'Name':'Verilife River North'}, {'Name':'Schaumburg Recreational'}]
Massachusetts_Recreational_Dispensaries = [{'Name':'Wareham Recreational'}, {'Name':'Shrewsbury Recreational'}]
VeriVIP = 'VeriVIP Members can redeem points in 200 points increments'
Social_Media = [{'Facebook': 'N/A'}, {'Instagram': '8,877 followers'}, {'Twitter': '2801 followers'}]
Illinois_Deals = [{'September23-30': 'Buy 2 AirPro Cartridges Get a free Airo Sport Battery'}, {'Deal': 'Buy 3 6PK Canntonics for $54'}]
PharmaCann = 'OWNS Verilife'
PharmaCann_Staff = [{'Name':'Bill McMenamy', 'Role':'Chief Revenue Officer'},{'Name':'Bryan Benavides', 'Role':'Director of Marketing'}, {'Name':'Gareld (Jerry) Eaton', 'Role':'Co-Founder'}, {'Name':'Robert Bank', 'Role':'Director of Wholesale Operations'}, {'Name':'Melissa B.', 'Role':'Marketing Manager'}, {'Name':'Jeff Langenbach', 'Role':'Head of Corporate Development'}, {'Name':'Jeff Thompson', 'Role':'Vice President of Manufacturing'}, {'Name':'Patrick Unzicker', 'Role':'Chief Financial Officer'}, {'Name':'Erika Salgado Guerra', 'Role':'VP of Marketing'}]
group_staff = groupby(PharmaCann_Staff, key=lambda x:x['Role'])
for key, value in group_staff:
    print(key, list(value))
Links=['https://www.linkedin.com/in/bbenavides/',
'https://www.linkedin.com/in/gareld-jerry-eaton-0089a68b/',
'https://www.linkedin.com/in/robert-bank-5aa708126/',
'https://www.linkedin.com/in/melissa-buckley/',
'https://www.linkedin.com/in/jeff-langenbach-78275a36/',
'https://www.linkedin.com/company/pharmacanninc/people/?keywords=CEO',
'https://www.linkedin.com/in/bill-mcmenamy-b964934/',
'https://www.linkedin.com/in/erikasguerra/']
