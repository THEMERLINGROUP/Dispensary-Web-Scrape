from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://ir.col-care.com/')
soup = BeautifulSoup(html_text, 'lxml')
hasInvestors = True
onDutchie = True