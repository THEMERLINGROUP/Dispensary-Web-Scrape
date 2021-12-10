from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.highquality.life/')
print(html_text, BeautifulSoup)
Socials = ['Leafly', 'Weedmaps', 'Twitter', 'Instagram']
Site = ['https://www.highquality.life/ourteam']
Rewards = 'Compassion Points Program'
Daily_Deals = [('Vet Discount- 5% OFF Daily'), ('Cyber Monday- 5% OFF online orders'), ('Try it Tuesdays- 10% OFF Staff picks'), ('Wax Wednesday- 10% OFF Participating vendors'), ('Thunder Thursdays- NO Tax on all Thunder Farms flower'), ('Forage Friday- Hand selected sale items'), ('Service Saturday- 15% OFF every Saturday for vets'), ('Silver Sunday- 10% OFF [55+]'), ('Patient Appreciation Day- 1st Saturday of month- 10% OFF storewide'), ('Communication Appreciation Day- 3rd Saturday of Month- 10% OFF Storewide')]
Our_Team = [{'Name':'Brock', 'Role':'Owner'}, {'Name':'Renee', 'Role':'Operations Director/Marketing Director'}, {'Name':'Steve', 'Role':'Financial Assistant'}, {'Name':'Harriet', 'Role':'Store Manager'}]
High_Quality_Team = groupby(Our_Team, key=lambda x:x['Role'])
for key, value in High_Quality_Team:
    print(key, list(value))

