from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.reefermadnesslounge.com/menu')
print(html_text, BeautifulSoup)
onDutchie = True
rewards_online = False 