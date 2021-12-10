from bs4 import BeautifulSoup
import requests
from itertools import groupby
html_text = requests.get('https://906fire.com/')
print(html_text, BeautifulSoup)
Rewards_Features = [('Get 150 points once you join'), ('1:1 Awards for every dollar spent'), ('Refer a friend and earn 150 bonus points when they make their first purchase'), ('VIP access to TFS deals, special offers, and events')]
Club_Rewards = [{'Points':150, 'Rewards':'$5 OFF'}, {'Points':250, 'Rewards':'$20 OFF'}, {'Points':500, 'Rewards':'$45 OFF'}, {'Points':1000, 'Rewards':'$100 OFF'}]
Current_Club_Rewards = groupby(Club_Rewards, key=lambda x:x['Rewards'])
for key, value in Current_Club_Rewards:
    print(key, list(value))
Links = ['https://906fire.com/our-story/']
Staff = [{'Name':'Logan Stauber', 'Role':'CEO'}, {'Name':'Stosh Wasik', 'Role':'CEO'}, {'Name':'Carlee Wasik', 'Role':'Human Resources Director'}, {'Name':'Montana McGeshick', 'Role':'Digital Content Manager'}, {'Name':'Bri Battisoni', 'Role':'Assistant Purchasing Manager'}, {'Name':'Trent Batchelor', 'Role':'CFO'}]
Fire_Staff = groupby(Staff, key=lambda x:x['Role'])
for key, value in Fire_Staff:
    print(key, list(value))
