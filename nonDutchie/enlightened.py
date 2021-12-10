from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://enlighteneddispensary.com/')
About = [{'Element':'Our Mission: to provide the most inclusive, knowledgeable, and comfortable experience possible.'}, {'Element':'Talk to Cannabis Guide'}, {'Element':'Rooted in Quality, highest standard'}, {'Element':'Communication'}]
Elements = groupby(About, key=lambda x:x['Element'])
for key, value in Elements:
    print(key, list(value))
Staff = [{'Name':'Lee Hatcher', 'Role':'Co-Owner'}, {'Name':'Dr. Dewayne Goldmon', 'Role':'Co-Owner'},{'Name':'Dr. Regina Thurman', 'Role':'Co-Owner'}, {'Name':'Stepanie Bush', 'Role':'General Manager'}, {'Name':'Maryam Salim', 'Role':'Marketing'}]
Staff_Basic_Position = 'Cannabis Guide'
Sites = ['https://www.linkedin.com/in/stephanie-bush-70434644/', 
'https://www.linkedin.com/company/enlightened-dispensary/']
Staff_Stats = groupby(Staff, key=lambda x:x['Name'])
for key, value in Staff_Stats:
    print(key, list(value))
Locations = ['Arkansas', 'Illinois']
Rewards_System_On_Website = False
on_Dutchie = False