from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://earthmed.com/')
soup = BeautifulSoup(html_text, 'lxml')

Locations = ['Chicago', 'Addison', 'Rosemont']
Rewards_System_Online = True
Points_System = [{'Points':0, 'Rewards':'Nothing' }, {'Points':600, 'Rewards': '(Medical), $30 off'}, {'Points':1000, 'Rewards':'(Recreational),$25 OFF'}]
Earth_Med_points_system = groupby(Points_System, key=lambda x:x['Rewards'])
for key, value in Earth_Med_points_system:
    print(key, list(value))
Sites = ['https://earthmed.com/rewards', 
'https://mywallet.deals/?m=ekup1sghru1rh1gh/#/rewards',
'https://www.linkedin.com/in/gus-koukoutsakis-60379511a/',
'https://www.linkedin.com/in/mike-perez-52016a/',
'https://earthmed.com/about/executive-team']
Daily_Specials = [{'Medical Mondays':'All Medical Patients Receive 10% Off Entire Order'}, {'Recreational Tuesdays':'All Recreational Customers Receive 10% Off Entire Order'}, {'Oil Wednesday':'10% Off All Concentrates, Vapes, Disposables'}, {'Tasty Thursday':'10% Off All Edibles'}, {'Flower Friday':'Select flower on SALE'}]
Mission_Statement = "EarthMed's focus is to provide a safe and legal venue for patients to receive treatment using Medical Cannabis."
Staff = [{'Name':'Mike Perez', 'Role':'Owner'}, {'Name':'Gus Koukoutsakis', 'Role':'Co-Founder/CEO'}]
#owned by Mindful Illinois LLC

