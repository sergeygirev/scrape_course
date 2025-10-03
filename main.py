import requests
from bs4 import BeautifulSoup

from time import sleep
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' }

def download(url):
    resp = requests.get(url, headers=headers, stream=True)
    r = open('/Users/sergeygirev/Desktop/images/' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()
    
def get_url():
    for count in range(1, 2):
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
            card_url = 'https://books.toscrape.com/catalogue/' + i.find('a').get('href')
            yield card_url

def array():       
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='col-sm-6 product_main')
        name = data.find('h1').text
        price = data.find('p', class_='price_color').text.replace('Â',  '')
        url_img = 'https://books.toscrape.com/' + soup.find('img')['src'].replace('../../', '')
        download(url_img)
        yield name, price, url_img