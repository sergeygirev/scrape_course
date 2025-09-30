import requests
from bs4 import BeautifulSoup

for count in range(1, 2):
    url = f'https://books.toscrape.com/catalogue/page-{count}.html'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for i in data:
        name = i.find('h3')
        full_name = i.h3.a['title']

        price = i.find('p', class_='price_color').text.replace('Â', '')

        url_img = 'https://books.toscrape.com/' + i.find('img')['src']

        print(full_name + '\n' + price + '\n' + url_img + '\n\n')