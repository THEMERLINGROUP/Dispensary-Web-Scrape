from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.tokyostarfish.com/tokyo-starfish-loyalty-program/')
soup = BeautifulSoup(html_text, 'lxml')
Sites = ["https://github.com/THEMERLINGROUP/DECENTMED/blob/master/DECENTMED.py", 
"https://github.com/THEMERLINGROUP/Applied-Python/blob/master/itertools.py",
"https://docs.google.com/spreadsheets/d/1Oexq1gvzGdyx7V78U9Cme5SNJsJmKTeMKM27XG3bdTg/edit#gid=0",
"https://docs.google.com/spreadsheets/d/1n78ad1Se2buxBdjnnmC_3LtkJUw8PX5cF2hWZGumcjI/edit#gid=0",
"https://www.tokyostarfish.com/"
"https://replit.com/@THEMERLINGROUP/Python#main.py",
"https://www.prnewswire.com/news-releases/enlightened-makes-its-cannabis-industry-debut-with-opening-of-four-arkansas-dispensaries-301152146.html",
""]


