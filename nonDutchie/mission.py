from itertools import groupby,product
Locations_Rec = [('Brookline'),('Calumet City')]
Deals = ['Calumet City']
Days = ['Magnificent Mondays:15%OFF with purchase 2+ cartridges/disposables',
'Terrific Tuesday:15%OFF [3.5,7,14,28g] flower',
'Wonderful Wednesday:FREE pre-roll with $150 purchase',
'Thoughtful Thursday:$5OFF EVERY $50 purchase',
'Fantastic Friday:15%OFFConcentrates/Extracts',
'Spectacular Saturday:15%OFF Edibles',
'Serene Sunday:25%OFF purchase of Tincture/Topicals',
'Student:10% OFF',
'OTHER:10%OFF Popular items']
prod = product(Deals,Days)
print(list(prod))
rewards_online = True
#Rewards in $
Rewards = [{'Points':0, 'Rewards':0}, {'Points':250, 'Rewards':15}]
Points = groupby(Rewards, key=lambda x:x['Rewards'])
for key, value in Points:
    print(key, list(value))
Sites = ['https://mywallet.deals/?m=fc1bkkphru1ws1b1/#/rewards',
         'https://missiondispensaries.com/rewards/',
         'https://www.linkedin.com/company/mission-dispensaries/',
         'https://www.linkedin.com/in/carlo-lookner-72324210b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_notifications%3BBkjLRXEOR1KUJ0LtQ0LDWg%3D%3D',
         'https://www.linkedin.com/in/sydney-derepentigny-ab22a61a4/?lipi=urn%3Ali%3Apage%3Ad_flagship3_notifications%3BBkjLRXEOR1KUJ0LtQ0LDWg%3D%3D',
         'https://www.linkedin.com/in/rebecca-gonzalez-931a661a9/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company%3BOKRCqc3TTD%2B4480CELgU8Q%3D%3D',
         'https://www.linkedin.com/in/derek-stewart-06114892/?lipi=urn%3Ali%3Apage%3Ad_flagship3_company%3BoH3MKuNfR6eH%2Fux0zL%2F%2Byg%3D%3D',
         'https://www.linkedin.com/in/harrison-doamaral/']
Owner = '4Front Ventures'
Staff = [{'Name':'Carlo Lookner', 'Role':'General Manager'}, {'Name':'Sydney Derepentigny', 'Role' :'General Manager'}, {'Name':'Gabriel Mendoza', 'Role':'Executive Vice President of Retail'}, {'Name':'Nick Couturier', 'Role':'VP of Operations'}, {'Name':'Rebecca Gonzales', 'Role':'General Manager'}, {'Name':'Harrison DoAmaral', 'Role':'Marketing Associate'}, {'Name':'Derek Stewart', 'Role':'VP of Retail Operations'}]
mission_staff = groupby(Staff, key=lambda x:x['Role'])
for key in mission_staff:
    print(key, list(value))
Four_Front_Ventures = [{'Name': 'Leo Gontmakh', 'Role':'CEO'}, {'Name':'Kris Krane', 'Role':'President'}, {'Name':'Andrew Thut', 'Role':'Chief Investment Officer'}, {'Name':'Joseph Feltham', 'Role':'Chief Operating Officer'}]
parent_company_staff = groupby(Four_Front_Ventures, key=lambda x:x['Role'])
for key in parent_company_staff:
    print(key, list(value))
parent_company_Directors = ['David Daily', 'Eric Rey', 'Kathi Lentzsch', 'Leo Gontmakher', 'Chetan Gulati', 'Roman Tkachenko']
