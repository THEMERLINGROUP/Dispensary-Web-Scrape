from itertools import groupby
Locations = [('Muskegon'), ('Edwardsburg'), ('Benton Harbor'), ('Battle Creek')]
Daily_Deals = [('Vets and Seniors get 10% OFF Daily'),
               ('Sunday 20% OFF'), ('20% off on your birthday!'),
               ('New customers get a special treat for a penny with a purchase of $20 or more')
               ]
Rewards_Program = 'Stalled'
Sites = ['https://www.linkedin.com/in/elizabeth-whitmyer-74548915b/',
         'https://us02web.zoom.us/j/2327455063']
Staff = [{'Name':'Daniel Paul', 'Role':'VP of Marketing'}, {'Name':'Alan Bonsett', 'Role':'Founder/President'}, {'Name':'Jennifer Mohnk', 'Role':'General Manager'}, {'Name':'Elizabeth Whitmyer', 'Role':'Assistant GM'}, {'Name':'Dylan Heikkila', 'Role':'Assistant GM'}]
NOBO_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in NOBO_Staff:
    print(key, list(value))
onDutchie = True