from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.lume.com/')
print(BeautifulSoup)
print(html_text)
onDutchie = True
link = ['https://dutchie.com/dispensary/lume-cannabis-co-kalamazoo',
'https://mywallet.deals/?m=ugu1zbgerubrughw/#/rewards',
        'https://www.linkedin.com/company/lume-cannabis-co/',
        'https://www.linkedin.com/in/johnathonkoweck/',
        'https://www.linkedin.com/in/zach-schreier-3a65159/',
        'https://www.linkedin.com/in/marcprichardson/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3Bbf1d0faf-e742-4310-9916-722911dcc845',
        'https://www.linkedin.com/in/william-bye-6068b73/',
        'https://www.linkedin.com/in/doug-hellyar-52449619a/',
        'https://www.linkedin.com/in/joseph-stankowski-64508713b/',
        'https://www.linkedin.com/in/adamserruys/']
Loyalty = [{'Points':0, 'Reward':0}, {'Points':150, 'Reward':'$5 OFF Entire Purchase'},
{'Points':300, 'Reward':'$25 OFF Entire Purchase & Lume T-shirt'}, {'Points':400, 'Reward':'Lume Hat'},
{'Points':500, 'Reward':'$40 OFF Entire Purchase'}, {'Points':650, 'Reward':'Lume Hoodie'},
{'Points':850, 'Reward':'$70 OFF Entire Purchase'}]
Lume_Loyalty = groupby(Loyalty, key=lambda x:x['Points'])
for key, value in Lume_Loyalty:
    print(key, list(value))
staff = [{'Name':'Johnathon Koweck', 'Role':'Director of Supply Chain'}, {'Name':'Heather(Martin) H.', 'Role':'Store Manager'},
{'Name':'Marc Richardson', 'Role':'Chief Information Officer'}, {'Name':'Zach Schreier', 'Role':'Director of Marketing'},
{'Name':'Joseph E. Rivera', 'Role':'Chief Financial Officer'}, {'Name':'John Gregory', 'Role':'Chief Marketing Officer'},
{'Name':'William Bye', 'Role':'Director of eCommerce'}, {'Name':'Doug Hellyar', 'Role':'CEO/President'},
{'Name':'Joseph Stankowski', 'Role':'District Manager'}, {'Name':'Dustin Mennie', 'Role':'Purchasing Manager'},
{'Name':'Scott Burnett', 'Role':'General Manager'}, {'Name':'Adam Serruys', 'Role':'Senior Software Developer'}, {'Name':'Dave Morrow', 'Role':'CEO'}]
Lume_staff = groupby(staff, key=lambda x:x['Role'])
for key, value in Lume_staff:
    print(key, list(value))

