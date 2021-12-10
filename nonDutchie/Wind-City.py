from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.windycitycannabis.com/')
print(html_text, BeautifulSoup)
SITES = ['https://www.instagram.com/windycitycannabis/', 'https://twitter.com/ILDispensaries',
'https://www.linkedin.com/in/steve-weisman-6712667/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFImjUBimXGz3I9YZzNVlqSC16u3HchCC8',
'https://www.linkedin.com/search/results/all/?keywords=windy%20city%20cannabis&origin=RICH_QUERY_SUGGESTION&position=0&searchId=8993d8bb-b44d-4913-9648-fbc3994eb301',
'https://www.linkedin.com/in/perrineknight/',
'https://www.linkedin.com/company/windy-city-cannabis/']
Sales = [{'Sunday':'Seniors 15% OFF, Everyone:Topicals&Tinctures 15%OFF'}, {'Monday':'Double Loyalty Points'}, {'Tuesday':'10% OFF edibles'}, {'Wednesday':'10% OFF vapes'}, {'Thursday':'15% OFF accessories'}, {'Friday/Saturday':'Spend $150 and get $10 off your next pre-order'}]
Locations = [('Homewoood'), ('Posen'), ('Litchfield'), ('Highwood'), ('Carpentersville'), ('Macomb')]
Socials = [{'Twitter': 1483}, {'Instagram':6436}]
rewards_on_site = False
Staff = [{'Name':'Steve Weisman', 'Role':'CEO'}, {'Name':'Joey Villagomez', 'Role':'General Manager'}, {'Name':'Perrine Knight', 'Role':'Chief Operating Officer'}, {'Name':'Wren Berger', 'Role':'VP of Retail'}, {'Name':'Kyla Hedrick', 'Role':'Head of Buying'}, {'Name':'Peter Smey', 'Role':'General Manager'}, {'Name':'Candice Cagala', 'Role':'General Manager'}, {'Name':'Matthew Woskey', 'Role':'General Manager'}, {'Name':'Graham Hughson', 'Role':'Head of Purchasing'}, {'Name':'Courtney Stupp', 'Role':'Retail Operations'}]
Windy_City_Cannabis_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in Windy_City_Cannabis_Staff:
    print(key, list(value))
