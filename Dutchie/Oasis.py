from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.oasiscannabisaz.com/')
print(html_text, BeautifulSoup)
Rewards_online =True
Rewards = [{'Tier1':150, 'Rewards':'(FREE Oasis dab cap), (FREE Haze or Lit Cannabis Lanyard),(FREE 1G of Oasis hyrbid or 1:1 blend preroll)'}, {'Tier2':300, 'Rewards':'(FREE Vape cartridge battery), (FREE Oasis promo T-Shirt), (FREE Strain-specific 1g pre-roll), (FREE Glass dab tool/Hand pendant), (5% OFF entire purchase)'},{'Tier3':500, 'Rewards':'(FREE 1/8 of Gold or Silver-tier flower),(FREE 5G Lit Cannabis, Vapen or Venom X Cartridge), (FREE 1G of HAZE cured batter, crumble, sugar wax or shatter), (FREE Oasis Navy blue team T-Shirt), (FREE 1G Venom shatter or cured crumble), ($10 OFF entire purchase), (FREE edible $20 value)'}, {'Tier4':750, 'Rewards':'(FREE edible $35 value), (FREE 1/8 Platinum flower), (FREE 5G Oasis JPAQ pre-roll Case), (FREE Oasis zip up hoodie), (FREE .5G Cresco. Timeless, or select cartridge), ($20 OFF entire purchase)'}, {'Tier5':1000, 'Rewards':'(FREE 1/8 Diamond-tier flower), (FREE 1G Timeless or select cartridge), (FREE Oasis Stainless steel water bottle), (FREE 1G Cresco concentrate [cured or live resin])'}]
Oasis_Rewards = groupby(Rewards, key=lambda x:x['Rewards'])
for key, value in Oasis_Rewards:
    print(key, list(value))
Links = ['https://www.linkedin.com/company/oasis-cannabis-az/people/',
         'https://iqagy.com/wallet/1362/y666reGKwS1dKcj1b-Mg3nDyJnfwbcuovW_Q-rwjoKDbfXGOCMI']
staff = [{'Name':'Rami Sweiss', 'Role':'Founder/President'}, {'Name':'Scottie Campbell', 'Role':'General Manager'}, {'Name':'Anders Mintz', 'Role':'Regional Marketing Director'}, {'Name':'Tayla Hamilton', 'Role':'Marketing Coordinator'}, {'Name':'Johnny Madrid', 'Role':'Assistant General Manager'}, {'Name':'Brittany Malcolm', 'Role':'Exectutive Assistant'}]
Oasis_Staff = groupby(staff, key=lambda x:x['Role'])
for key, value in Oasis_Staff:
    print(key, list(value))
onDutchie = True
