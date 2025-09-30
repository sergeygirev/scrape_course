import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

name = data.find('h3')
full_name = data.h3.a['title']

price = data.find('p', class_='price_color').text.replace('Â', '') 

url_img = 'https://books.toscrape.com/' + data.find('img')['src']