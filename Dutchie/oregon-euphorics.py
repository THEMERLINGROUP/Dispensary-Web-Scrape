from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.oregoneuphorics.com/')
print(html_text, BeautifulSoup)
onDutchie = True
Links = ['https://www.linkedin.com/search/results/all/?keywords=Oregon%20Euphorics', 
         'https://www.linkedin.com/in/taylor-rembowski-217924173/',
         'https://www.linkedin.com/in/kira-bellis-07377a171/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACje3tcBxzTTL1wtKU8k4uN2hN6F411k1V4']
Staff = [{'Name':'Taylor Rembowski', 'Role':'Owner'}, {'Name':'Kira Bellis', 'Role':'Assistant Manager'}, {'Name':'Mark Capps', 'Role':'Managing Member'}]
Oregon_Euphorics = groupby(Staff, key=lambda x:x['Role'])
for key, value in Oregon_Euphorics:
    print(key, list(value))
