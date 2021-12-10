from bs4 import BeautifulSoup
import requests
from itertools import groupby
onDutchie = True
html_text = requests.get('https://highwirefarms.com/cannaco-op/')
print(html_text, BeautifulSoup)
rewards_online = 'Canna CO-Op'
canna_co_op_pricing = [('Flower 10% OFF'), ('Concentrates 20% OFF'), ('Edibles 20% OFF'), ('Vapes 20% OFF'), ('Accessories 20% OFF')]
canna_co_op_benefits = [('Exclusive CANNA CO-OP Pricing'), ('Special Member only-specials'),
('Free mixers and meetings'), ('Unique CANNA CO-OP Swag'), ('Special Member Only Events')]
canna_co_op_membership_details = [{'Price Monthly':20}, {'MUST':'Debit/Credit card must be on file'},
{'Automatic Payments':True}]
links = ['https://www.linkedin.com/in/eric-kennedy-50511612/']
staff = [{'Name':'Eric Kennedy', 'Role':'Co-Founder/Chief Operating Officer'}, {'Name':'Tony Ratliff', 'Role':'Co-Founder'}]
Highwire_Farms_Staff = groupby(staff, key=lambda x:x['Name'])
for key, value in Highwire_Farms_Staff:
    print(key, list(value))
