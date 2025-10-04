from requests import Session
from bs4 import BeautifulSoup
from time import sleep
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' }

work = Session()
work.get('https://quotes.toscrape.com', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')