from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://gohatch.com/')
print(html_text, BeautifulSoup)
Locations = [{1:'Addison'}, {2:'Wheeling'}]
onDutchie = True
Sites = ['https://dutchie.com/dispensary/hatch',
'https://gohatch.com/hatch-rewards-program/',
'https://mywallet.deals/?m=kbchbzkfru1rbgcu/#/profile',
'https://www.linkedin.com/in/sarah-zelman/',
'https://www.linkedin.com/company/hatchdispensary/',
'https://www.linkedin.com/search/results/all/?keywords=Mindful%20Illinois%2FHatch']
Aeropay = True
Password_For_Rewards = False
Points = [{'Points': 0, 'Rewards':'NONE'}, {'Points':200, 'Rewards':'$5 OFF Purchase'}, {'Points':1000, 'Rewards':'$25 OFF Purchase'}]
Staff = [{'Name':'Sarah Zelman', 'Role':'Senior Marketing Manager'}, {'Name':'Kaitlin Smith', 'Role':'General Manager'}, {'Name':'Eric Fisher', 'Role':'Chief Financial Officer'},{'Name':'Brian Baker', 'Role':'VP of Operations'}]
#owned by Mindful Illinois LLC
HATCH_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in HATCH_Staff:
    print(key, list(value))
