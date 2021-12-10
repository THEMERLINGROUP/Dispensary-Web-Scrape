from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://maribisllc.com/home.html')
from itertools import groupby, product
Locations=['Maribis of Chicago', 'Maribis of Westchester', 'Maribis of Springfield', 'Maribis of Springfield West']
Numbers=[1,2,3,4]
prod = product(Locations, Numbers)
print(list(prod))
Rewards_Online = False
Sites = ['https://www.dnb.com/business-directory/company-profiles.maribis_llc.703b307ef18c39dc1cbec19d2d7efd09.html',
'https://www.bbb.org/us/il/chicago/profile/medical-marijuana-dispensaries/maribis-of-chicago-medical-marijuana-dispensary-0654-90029913/details']
staff = [{'Name':'Dan Linn', 'Role':'General Manager'}, {'Name':'Laurel Dineff.', 'Role':'Owner'}]
Found_Decision_Maker = False
onDutchie = False