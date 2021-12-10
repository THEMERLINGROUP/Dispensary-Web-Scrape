from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://euphoriawellnessnv.com/')
print(BeautifulSoup)
print(html_text)
rewards_levels = [('Bud'), ('VIP'), ('Diamond'), ('Elite')]
Points = [{'Bud':1}, {'VIP':1.5}, {'Diamond':2}, {'Elite':2.5}]
staff = [{'Name':'Joe Lamarca', 'Role':'Owner'}, {'Name':'Larry Doyle', 'Role':'Owner'}]
euphoria_staff = groupby(staff, key=lambda x:x['Name'])
for key, value in euphoria_staff:
    print(key, list(value))
