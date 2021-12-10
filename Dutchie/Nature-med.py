from bs4 import BeautifulSoup
import requests
print(BeautifulSoup)
html_text = requests.get('https://www.naturemedaz.com/shop-online/?')
onDutchie = True
rewards_online = False