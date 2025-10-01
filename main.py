import requests
from bs4 import BeautifulSoup

from time import sleep
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' }

for count in range(1, 3):
    sleep(2)
    url = f'https://books.toscrape.com/catalogue/page-{count}.html'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    # for i in data:
    #     name = i.find('h3')
    #     full_name = i.h3.a['title']

    #     price = i.find('p', class_='price_color').text.replace('Â', '')

    #     url_img = 'https://books.toscrape.com/' + i.find('img')['src']

    #     print(full_name + '\n' + price + '\n' + url_img + '\n\n')
    for i in data:
        card_url = i.find('a').get('href')
        print(card_url)