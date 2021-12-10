from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.consumecannabis.com/')
print(html_text, BeautifulSoup)
Recreational_Locations = [('Oakbrook Terrace'), ('Carbondale')]
Socials = [{'Twitter': 408}, {'YouTube':126}, {'Pinterest':73}]
Staff = [{'General Manager': 'Jen Reidinger'}]
