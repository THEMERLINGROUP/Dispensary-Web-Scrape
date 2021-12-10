from itertools import groupby, accumulate
locations = [{'Name': 'Box Factory', 'Location': '542NW Arizona Ave. Bend, OR 97703', 'Number': '(541)797-2110'}, {'Name': 'Tokyo South','Location': '61230 S HWY 97. Bend,OR 97702', 'Number':'(541)241-2387'}, {'Name': 'Tokyo SE 3rd ST','Location': 'Tokyo SE 3rd ST Bend,OR', 'Number': '(541)678-5199'}, {'Name': 'Tokyo Starfish Salem', 'Location':'1695 Center ST NE Salem,OR 97301', 'Number':'971-304-7614'}]
Tokyo_Starfish_locations = groupby(locations, key=lambda x:x['Number'])
for key, value in Tokyo_Starfish_locations:
    print(key, list(value))
Monthly_Deals_All_Locations = ['All PAX pods are $7 off(9/27-10/3)', '50% off white label extracts', 'Friday/Saturdays 15% off Tokyo House grown flower', '10% veteran discount', 'Monday-10% Industry Discount', 'Loyalty Club Signup-10% off next purchase', 'Vendor Highlight week-20-30%', 'Tinctures and jointment on sale']
acc = accumulate(Monthly_Deals_All_Locations)
print(Monthly_Deals_All_Locations)
print(list(acc))
Salem_Discounts = [{'Flower Friday': '15% off ALL flower'}, {'Shattered Saturday': '10% Off ALL Extracts & Cartridges'}, {'Mondays Suck': '20% off storewide'}, {'Additional': '10% Off All Online Orders:(7 days a week). This is a stackable discount. Example: if you order a Shatterday Special (10% off) online from tokyostarfish.com or dutchie.com (+10% off) = 20% total discount for that order.'}]
print(Salem_Discounts)
Tokyo_Starfish_Bend = "First Bud and Breakfast in Bend,OR"
Points_System = [{'Points':0, 'Rewards':'Nothing' }, {'Points': 100, 'Rewards':'Tokyo Lighter'}, {'Points':250, 'Rewards': '5$ OFF glass, accessories, apparel'}, {'Points':300, 'Rewards':'Tokyo Socks'}, {'Points':500, 'Rewards':'Tokyo Battery'}, {'Points':750, 'Rewards':'Tokyo T-Shirt, 15$ OFF glass, accessories, apparel'}, {'Points':1000, 'Rewards':'Tokyo Hat/Beanie, 20$ OFF glass, accessories, apparel'}, {'Points':2000, 'Rewards':'15% OFF purchase, $50 OFF glass, accessores, apparel'}, {'Points':3000, 'Rewards':'$75 OFF Glass, Accessories, Apparel'}, {'Points':6000, 'Rewards':'$150 Off Glass, Accessories, Apparel'}]
Tokyo_Starfish_points_system = groupby(Points_System, key=lambda x:x['Rewards'])
for key, value in Tokyo_Starfish_points_system:
    print(key, list(value))
#Pin Club Bio on Twitter: 3,333 unique vintage #NFT pins for Collectors by Collectors coming on the #Solana blockchain winter 2021.
Social_Media = [{'Twitter': '92 Followers, Follow Pin CLub'}, {'Instagram': '7228 Followers'}]
Reward = 'Ranked Bend, OR best dispensary'
Staff = [{'Marketing': 'Jason Shurtz'}, {'Co-Owner':'Jason McAlister'}, {'Co-Owner':'Kale Gray'}, {'Co-Owner': 'Keith Legum'}, {'Co-Owner': 'Gary Bracelin'}]
Jason_Shultz_Linkedin = "https://www.linkedin.com/in/jasonshurtz/"
Ownership = [{'Name':'Jason McAllister', 'Role': 'In charge of operations'}, {'Name':'Kale Gray', 'Role':'Marketing and Branding'}, {'Name':'Keith Legum', 'Role':'Architecture, Design, building'}, {'Name':'Gary Bracelin', 'Role':'Buying and distribution'}]
Owners = groupby(Ownership, key=lambda x:x['Role'])
for key, value in Owners:
    print(key, list(value))
#Target Marketing (NOT Director of Marketing) Director of Marketing is decision maker
Plan = ['Find Coordinator', 'Connect with Director of Marketing', 'Create 2 sentence introduction', 'Message is the most important thing']
Links = ['https://www.linkedin.com/in/jasonshurtz/',
'https://dutchie.com/dispensary/tokyo-starfish-salem']
onDutchie = True
