from itertools import groupby
Locations = [{'State':'Pennsylvania', 'Location-Volume':15}, {'State':'Illinois', 'Location-Volume':4}, {'State':'California', 'Location-Volume':2}, {'State':'Virginia', 'Location-Volume':1}, {'State':'Massachusetts','Location-Volume':2}]
location_group = groupby(Locations, key=lambda x:x['Location-Volume'])
for key, value in location_group:
    print(key, list(value))

Hello_Club = [{'Points':0, 'Dollars-Off':0}, {'Points':200, 'Dollars-Off':10}, {'Points':1000, 'Dollars-Off':60}, {'Points':2000, 'Dollars-Off':140}]
Rewards = groupby(Hello_Club, key=lambda x:x['Dollars-Off'])
for key, value in Rewards:
    print(key, list(value))
Owners = 'Jushi Holdings'
OnDutchie = True
Sites = ['https://www.linkedin.com/company/jushi-inc/people/?keywords=CEO',
         'https://www.linkedin.com/in/dremenator/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3B19e9d292-f181-46d1-a838-0a6892040364',
         'https://www.linkedin.com/in/bambachk/']
Jushie_Staff = [{'Name':'James Cacioppo', 'Role':'Co-Founder'}, {'Name':'Ryan Cook', 'Role':'Executive VP of Operations'}, {'Name':'Andreas Neumann', 'Role':'Chief Creative Officer'}, {'Name':'Kimberly Bambach', 'Role':'Chief Financial Officer'}, {'Name':'Brendon Lynch', 'Role':'Executive VP of Retail'}, {'Name':'Gabe Cohen', 'Role':'Vice President'}, {'Name':'Trent Woloveck', 'Role':'Chief Commercial Director'}, {'Name':'Mychal D.', 'Role':'General Manager'}, {'Name':'Ashley Esper', 'Role':'Senior Director Commerical Operations'}, {'Name':'Todd B. Green', 'Role':'Director of Investor Relations'}, {'Name':'Michael Perlman', 'Role':'Executive VP of Investor Relations'}, {'Name':'Niki Mohrlant', 'Role':'Senior Director of Operations'}]
