import json
from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.medmen.com/')
print(BeautifulSoup)
print(html_text)
def write_json(data, filename="Dutchie-vs-Medmen.JSON"):
    with open(filename, "r") as a:
        json.dump(data, a, indent=4)
    with open("Dutchie-vs-Medmen.JSON") as json_file:
        data = json.load(json_file)
    write_json(data)
Buds_Rewards = [{'Points':0, 'Value':0}, {'Points':200, 'Value':'$5 in Rewards'}]
Medmen_Rewards = groupby(Buds_Rewards, key=lambda x:x['Value'])
for key, value in Medmen_Rewards:
    print(key, list(value))
links = ['https://www.medmen.com/rewards',
         'https://www.linkedin.com/in/abierman?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAVQdaIBA-z4GCcLHYauQ3F-befHvcxlk7s&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BIUe2fSZGRUK1PPc8wkkL8Q%3D%3D',
         'https://www.linkedin.com/in/karen-torres-38147125/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3Bba2183c3-772d-40d5-98e3-1acf957e9a42',
         'https://www.linkedin.com/in/mindi-basha-1038231b/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3Bba2183c3-772d-40d5-98e3-1acf957e9a42',
         'https://www.linkedin.com/company/the-medmen/people/',
         'https://www.linkedin.com/in/reneerosenau/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3Bba2183c3-772d-40d5-98e3-1acf957e9a42']
staff = [{'Name':'Adam Biermman', 'Role':'Co-Founder'}, {'Name':'Tyson Rossi', 'Role':'Senior VP of Product and Revenue'}, {'Name':'Karen Torres', 'Role':'Head of Supply Chain Operations'}, {'Name':'Mindi Basha', 'Role':'VP of Retail'}, {'Name':'Renee Rosenau', 'Role':'District Manager'}, {'Name':'Greg Lucchese', 'Role':'Operations Lead'}]
Medmen_staff = groupby(staff, key=lambda x:x['Role'])
for key, value in Medmen_staff:
    print(key, list(value))
    
