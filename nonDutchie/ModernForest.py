from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://www.modernforestlife.com/")
print(html_text, BeautifulSoup)
rewards = "Punch Card"
rewards_on_webpage = False
