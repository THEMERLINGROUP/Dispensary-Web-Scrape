from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://awholdings.com/')
print(html_text, BeautifulSoup)
States = [{'Ohio':1}, {'Illinois':5}, {'Massachusetts':3}, {'Michigan':6}, {'New Jersey':2}]
Activism = 'Last Prisoner Project Partnership'
Sites = ['https://www.instagram.com/ascendwellnessholdings/', 'https://awholdings.com/',
'https://www.linkedin.com/in/abner-kurtin-78b8b66b/','https://www.linkedin.com/company/ascendwellnessholdings/people/', 'https://www.linkedin.com/in/michael-towey-19259a157/',
'https://www.linkedin.com/in/frank-perullo-9072688/',
'https://www.linkedin.com/in/kolivastro/',
'https://www.linkedin.com/in/joe-gullia/',
'https://www.linkedin.com/in/mark-youngworth/',
'https://www.linkedin.com/company/ascendwellnessholdings/people/?keywords=marketing']
Socials = [{'Instagram':'7934 Followers'}, {'Linkedin':'241 Employees'}]
Staff = [{'Name':'Abner Kutin', 'Role':'Founder'}, {'Name':'Michael Towey', 'Role':'VP of Cultivation'}, {'Name':'Frank Perullo', 'Role':'Chief Strategy Officer'}, {'Name':'Kathleen Olivastro', 'Role':'Regional Director'}, {'Name':'David Jerome', 'Role':'Senior VP of Operations'}, {'Name':'Chris Melilo', 'Role':'Chief Revenue Officer'}, {'Name':'Jake Moote', 'Role':'General Manager'}, {'Name':'Joe Gullia', 'Role':'Senior VP of Retail'}, {'Name':'Mark Youngworth', 'Role':'Senior VP of Marketing'}, {'Name':'Don Sprenkle', 'Role':'VP of Wholesale Sales'}, {'Name':'Cassandra Gundy', 'Role':'Senior Manager Digital and Consumer Engagement'}, {'Name':'Don Shaefer', 'Role':'VP of Retail'}, {'Name':'Brendan Antonacci', 'Role':'Marketing Coordinator S. Illinois'}, {'Name':'Alexander Schratz', 'Role':'Michigan Marketing Coordinator'}]
Staff_Ascend_Wellness_Holdings = groupby(Staff, key=lambda x:x['Role'])
for key, value in Staff_Ascend_Wellness_Holdings:
    print(key, list(value))
revenue_Raised_2020 = 68000000
onDutchie = False
rewards_On_Page = False
