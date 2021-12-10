from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.greengatechicago.com/')
print(html_text, BeautifulSoup)
Sites = ['https://twitter.com/greengatechi?lang=en',
'https://www.instagram.com/greengatechicago/?igshid=f2m37wnmatyi',
'https://www.linkedin.com/in/chassidy-crowder-86433443/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAkgJswBLkM_HDtSMNoASgB69NjKb55nkjQ',
'https://www.linkedin.com/in/colin-miller-952908b5?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABiEd04B46TNjtmHudAToEsboDMx7xBSboA&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people_load_more%3BFWJ1UbEtREiE7IbtFkAY9w%3D%3D']
socials = [{'Twitter':370}, {'Instagram':2221}]
rewards_Program_ON_site = False
Staff = [{'Name':'Chassidy Crowder', 'Role':'General Manager'}, {'Name':'Bob Kingley', 'Role':'Owner'}, {'Name':'Colin Miller', 'Role':'Inventory Manager'}]
nuEra_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in nuEra_Staff:
    print(key, list(value))
onDutchie = False