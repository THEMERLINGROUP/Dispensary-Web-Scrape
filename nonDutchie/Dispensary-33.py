from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://dispensary33.com/')
print(html_text, BeautifulSoup)
Sites = ['https://www.leafly.com/dispensary-info/dispensary-33',
'https://www.instagram.com/dispensary33/',
'https://twitter.com/dispensary33/',
'https://weedmaps.com/dispensaries/dispensary-33',
'https://www.linkedin.com/company/dispensary33/people/',
'https://www.linkedin.com/in/abigail-watkins-95a599143/']
Locations = [('D33 West Loop:Recreational'), ('D33 in Andersonville: Medical/Recreational')]
Socials = [{'Instagram':20000}, {'Twitter':6162}]
Supports_LGBTQ = True
Staff = [{'Name':'Scott Cramer', 'Role':'Marketing Coordinator'}, {'Name':'Abigail Watkins', 'Role':'Marketing Director'}, {'Name':'Zachary Zises', 'Role':'Co-Founder'}, {'Name':'Paul Lee', 'Role':'Co-Founder'}, {'Name':'Kristie Zises', 'Role':'Co-Founder'}]
Dispensary33_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in Dispensary33_Staff:
    print(key, list(value))
