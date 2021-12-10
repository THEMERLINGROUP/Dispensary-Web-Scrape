from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://silvercreekdispensary.com/?')
print(html_text)
print(BeautifulSoup)
onDutchie = True
