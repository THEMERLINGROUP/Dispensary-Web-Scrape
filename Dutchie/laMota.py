from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://www.oregoneuphorics.com/')
print(html_text, BeautifulSoup)
onDutchie = True
rewards_on_page = False