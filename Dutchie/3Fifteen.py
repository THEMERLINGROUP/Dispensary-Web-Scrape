from bs4 import BeautifulSoup
from itertools import groupby
import requests
html_text = requests.get('https://3fifteen.com/')
BeautifulSoup
print(html_text)
onDutchie = True
Rewards = [{'Points':100, 'Tier':'1, [$5 OFF Entire purchase]'}, {'Points':200, 'Tier':'2, [$10 OFF Entire Purchase]'}, {'Points':300, 'Tier':'3, [$15 OFF Entire Purchase]'}, {'Points':400, 'Tier':'4, [$20 OFF Entire Purchase]'}, {'Points':500, 'Tier':'5, [$25 OFF Entire Purchase]'}, {'Points':600, 'Tier':'6, [$30 OFF Entire purchase]'}, {'Points':700, 'Tier':'7, [$35 OFF Entire Purchase]'}, {'Points':800, 'Tier':'8, [$40 OFF Entire Purchase]'}, {'Points':900, 'Tier':'9, [$45 OFF Entire Purchase]'}, {'Points':1000, 'Tier':'$50 OFF Entire Purchase'}]
315 = groupby(Rewards, key=lambda s:s['Tier'])
for key, value in 315:
    print(key, list(value))
Owner = 'Skymint INC.'
staff = [{'Name':'Donnel Cravens', 'Role':'Director of Retail Operations'}, {'Name':'Laura Hufshmidt', 'Role':'Marketing Director'}, {'Name':'Darren Gacicia', 'Role':'Chief Financial Officer'}, {'Name':'Michael Krefman', 'Role':'Chief Merchandising Officer'}, {'Name':'Cameron Baker', 'Role':'General Manager Operations'}, {'Name':'Jeff Radway', 'Role':'CEO of Skymint'}]
three_fifteen_staff = groupby(staff, key=lambda x:x['Name'])
for key, value in three_fifteen_staff:
    print(key, list(value))

link = ['https://www.linkedin.com/in/donnell-cravens-mba-a3562455?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAupGskBsfLEFu8rytgmwJFbOJIVlJiWyKI&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BntHr0lLXR7WqwCt%2BKTERzw%3D%3D',
        'https://www.linkedin.com/in/lehufschmidt?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFriqwBXKeWnfwLa24SnbZPS5UrEIFko1c&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BntHr0lLXR7WqwCt%2BKTERzw%3D%3D',
        'https://www.linkedin.com/company/3fifteen-cannabis/']
