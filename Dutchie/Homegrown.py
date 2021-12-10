from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.homegrownpnw.com/')
print(html_text, BeautifulSoup)
Links = ['https://dutchie.com/stores/homegrown-beaverton']
onDutchie = True
