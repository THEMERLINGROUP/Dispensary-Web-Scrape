from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://thethccenter.com/')
print(html_text, BeautifulSoup)
sites = ['https://www.facebook.com/TheHerbalCareCenter/', 'https://www.google.com/search?ludocid=10226010512739684620&hl=en-US&q=The%20Herbal%20Care%20Center%201301%20South%20Western%20Avenue%20Chicago,%20Illinois%2060608&_ga=2.232999390.1763083469.1529713008-1430146092.1526837984#fpstate=lie&lrd=0x880e2d70513c9233:0x8dea1661b142510c,3,,,',
'https://www.linkedin.com/in/michael-mandera-24a80b59/',
'https://thethccenter.com/patient-loyalty/',
'https://www.dnainfo.com/chicago/20170112/medical-district/perry-mandera-the-herbal-care-center-vips-strip-club-medical-marijuana-dispensary-medical-district/']
Location = [{'1301 S Western Ave Chicago,IL 60608'}, {'Phone':'773-724-4200'}]
Socials = [{'Facebook':'2167 Likes', 'Facebook':'2488 Followers'}, {'Twitter':'384 Followers'}]
Staff = [{'Name':'Nicholas/Michael Mandera', 'Role':'General Manager'}, {'Name':'Perry Mandera', 'Role':'Owner'}]
staff_THCC = groupby(Staff, key=lambda x:x['Role'])
for key, value in staff_THCC:
    print(key, list(value))
Everyday_Discount_Programs = [('Seniors: 10% discount'), ('Veterans: 10% discount'), ('Compassion Program:We welcome any patient with financial hardships to apply for our Compassion Program. This program offers discounted products and/or grants for patients that are experiencing tough financial times. Please request a compassion program application from our receptionist on your next visit. Once completed and submitted, these applications are reviewed and decided upon on a case by case basis.')]
onDutchie = False