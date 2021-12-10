from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://pureoptions.com/')
print(BeautifulSoup)
print(html_text)
onDutchie = True
links = ['https://pureoptions.com/pure-perks/',
         'https://www.linkedin.com/search/results/people/?currentCompany=%5B%2275426220%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH',
         'https://www.linkedin.com/in/nickpopoff?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABad8_cBBHiXX9hfWFdf5gR3kW0AwoSNZnI&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BHOOzJAl%2FRJa3oEoj3Pe9dw%3D%3D',
         'https://www.linkedin.com/in/cassmattyholdburg?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACRD5MYB2ipiE1dU_IICu4PDmU_xrBri0Hw&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BHOOzJAl%2FRJa3oEoj3Pe9dw%3D%3D',
         'https://www.linkedin.com/in/maggie-kinney-093ba2b0?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABerO-8B6AywpQP-61Fy2iY3OFM3B9QDTZU&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3Bx%2BFSLHoiSpmn%2BP36cMVAjw%3D%3D']
points = [{'Points': 0, 'Value': 0}, {'Points': 250, 'Value': 'Pre-roll or T-shirt or $10 off'},
{'Points':500, 'Value':'1 edible[$20 VALUE] or Hat or $20 OFF'}, {'Points':750, 'Value':'Longsleeve T-shirt, Edibles[2x $40 VALUE] or $30 OFF'},
{'Points':1000, 'Value':'Vape Cart or 4 pre-rolls[Mix & Match]$40 VALUE'}, {'Points':1500, 'Value':'1/8 of flower or Hoodie or $50 OFF'},
{'Points':2500, 'Value':'2 1/8s or Concentrate 1G [$75 OFF]'}, {'Points':5000, 'Value':'Half Ounce of Flower or $200 Fieldhouse Gift Card or $200 OFF'},
{'Points':10000, 'Value':'Ounce of flower or 5G Concentrate or $250 OFF'}, {'Points':250000, 'Value':'Detroit Red Wings Suite[single game] or FREE Cannabis for a year[2 Ounces per month]'}]
Pure_Perks = groupby(points, key=lambda x:x['Points'])
for key, value in Pure_Perks:
    print(key, list(value))
staff = [{'Name':'Nick Popoff', 'Role':'General Manager'}, {'Name':'James Barr','Role':'Co-Owner'},
{'Name':'Sam Usman Jr.', 'Role':'Co-Owner'}, {'Name':'Cassandra Holdburg', 'Role':'PR/Marketing'},
{'Name':'Maggie Kinney', 'Role':'Retail Operations Supervisor'}, {'Name':'Trevor Kildea', 'Role':'Senior Assistant Manager'}]
Pure_Options_Staff = groupby(staff, key=lambda s:s['Role'])
for key, value in Pure_Options_Staff:
    print(key, list(value))
