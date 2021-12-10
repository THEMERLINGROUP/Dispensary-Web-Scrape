from bs4 import BeautifulSoup
import requests
from itertools import groupby
print(BeautifulSoup)
html_text = requests.get('https://northcoastprovisions.com/')
links = ['https://northcoastprovisions.com/deals-specials-at-north-coast-provisions/#loyaltyrewards',
         'https://www.linkedin.com/in/alexander-mckelvie-a60110104?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABpbYugBDelg6MT79Y-95ggtuTM9slMjt6U&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BIuaaeedhTyW563ZZwOyqlQ%3D%3D',
         'https://www.linkedin.com/search/results/people/?keywords=north%20coast%20provisions&origin=CLUSTER_EXPANSION']
Deals = [{'Medible Monday': '15% OFF all edibles'}, {'Topshelf Tuesday':'15% OFF all premium/top-shelf flower'},
{'Waxy Wednesday':'15% OFF all concentrates and cartridges'}, {'Arborside T-shirt Thursday':'Flower $16G^ 15% OFF'},
{'Four Gram Friday':'All 1/8 Flower purchased weighed heavy to 4G'}, {'Student/Senior Saturday':'15% OFF for students/seniors'}, {'Sunday':'15% OFF 10am-2pm'}]
Rewards = [{'Points':0, 'Value':0}, {'Points':500, 'Value':'$25 OFF order'}]
North_Coast_Rewards = groupby(Rewards, key=lambda s:s['Points'])
for key, value in North_Coast_Rewards:
    print(key, list(value))
staff = [{'Name':'Alexander McKelvie', 'Role':'General Manager'}, {'Name':'Sean McQuarrie', 'Role':'CEO'}]
North_Coast_Staff = groupby(staff, key=lambda x:x['Role'])
for key, value in North_Coast_Staff:
    print(key, list(value))

