from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_Text = requests.get('https://www.skymint.com/')
print(html_Text, BeautifulSoup)
points_update = 'You get one per item'
Links = ['https://www.skymint.com/rewards/',
         'https://www.linkedin.com/search/results/people/?keywords=Skymint%20&origin=GLOBAL_SEARCH_HEADER']
points = [{'Points':0, 'Value':0}, {'Points':250, 'Value':'FREE Pre-roll, OR 1 T-shirt, OR Skymint Gummies, OR $10 OFF'},
{'Points':500, 'Value':'2 Pre-rolls, OR 1G flower, OR Jolly Gummies, OR $20 OFF'},
{'Points':750, 'Value':'Skymint Crew Neck Sweatshirt, OR 1/8 Flower, OR 1G Concentrate, OR $30 OFF'},
{'Points':1000, 'Value':'5 Pre-rolls, OR Pre-roll + 1/8, OR Skymint or Jolly Gummies, OR $40 OFF'},
{'Points':2000, 'Value':'2 0.5G Live Resin Concentrate, OR 2 Skymint x DNA 1/8 Flower, OR Any Marley Item, OR $80 OFF'}]
Sky_Points = groupby(points, key=lambda x:x['Points'])
for key, value in Sky_Points:
    print(key, list(value))
staff = [{'Name':'Jeffrey Radway', 'Role':'CEO'}, {'Name':'Connor Jacobs', 'Role':'Social and Digital Marketing Manager'}, {'Name':'Shelby Hooper', 'Role':'Senior Manager of Operations'}, {'Name':'Aimee Michalak', 'Role':'Senior Director of Marketing'}]
skymint_staff = groupby(staff, key=lambda s:s['Name'])
for key, value in skymint_staff:
    print(key, list(value))
onDutchie = True

