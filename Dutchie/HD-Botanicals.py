from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://hdbotanicals.com/')
soup = BeautifulSoup(html_text, 'lxml')
Deals = [{'Monday':'Edibles 15% off'}, {'Tuesday':'Topicals 15% off'}, {'Wednesday':'Wax and oils 15% off'}, {'Thursday':'Tinctures 15% OFF'}, {'Friday':'15% OFF Flower and prerolls'}, {'Saturday':'15% OFF Shatter/Oils'}, {'Sunday':'15% off CBD 1:1+'}, {'OMMP Medical/Veterans':'15% off All products'}, {'Full Loyalty Card':'20% off All Products'}]
Online_Ordering = True
Cash_Or_Card = "Cash only"
Owners = ['Matt Toepfer', 'Jill Toepfer']
Sites_To_Use = ['https://hdbotanicals.com/menu.html?',
'https://hdbotanicals.com/about-company.html',
'https://www.linkedin.com/in/matt-toepfer-77414a31/']
onDutchie = True
Social_Media = [{'Instagram':'1085 followers'}]
Ties_to_brand_Viola = True
Locations = 1
phone = ['541-536-0432']

