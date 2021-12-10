from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.midwaydispensary.com/')
print(html_text, BeautifulSoup)
online_store = 'Dispense'
rewards_online = False
Sites = ['https://www.midwaydispensary.com/', 'https://www.linkedin.com/search/results/all /?keywords = Midway % 20Dispensary',
         'https://www.linkedin.com/in/neal-mcqueeney-3039336/',
         'https://www.linkedin.com/in/ryan-mcqueeney-66310399?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABTWs-sB3B0dQIEOlV1zPgUN7BA7cAvaVVM&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BPwmwEcHeTLOWGzuR9RZ1Dg%3D%3D']
Staff = [{'Name':'Ryan McQueeney', 'Role':'Head of Strategy'}, {'Name':'Neal McQueeney', 'Role':'Agent in Charge'}]
Midway_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in Midway_Staff:
    print(key, list(value))
