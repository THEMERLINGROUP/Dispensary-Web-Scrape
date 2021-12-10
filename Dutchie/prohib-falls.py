from bs4 import BeautifulSoup
from itertools import groupby
import requests
html_text = requests.get('https://prohibitionfallsoregon.com/')
print(BeautifulSoup)
print(html_text)
onDutchie = True
Deals = [{'Deal':'Fire Sale Friday', 'Offering':'10% OFF ALL DAY'}, {'Deal':'Veterans', 'Offering':'Code:["VETERAN15"] 15% OFF'}, {'Deal':'Seniors[65+]', 'Offering':'Code:["SENIOR10"] 10% OFF'}]
Daily_Deals = groupby(Deals, key=lambda x:x['Offering'])
for key, value in Daily_Deals:
    print(key, list(value))
