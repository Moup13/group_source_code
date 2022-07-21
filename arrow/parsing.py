import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://minfin.com.ua'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

CSV = 'cards.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-item')

    cards = []
    for item in items:
        cards.append({

            'title': item.find('div', class_='title').get_text(strip=True),
            'link_product': HOST + item.find('div', class_='title').get('href'),
            'brand': item.find('div', class_='brand').get_text(strip=True),
            'card_img': HOST + item.find('div', class_='image').find('img').get(),
        })
    return cards


def s_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Ссылка', 'Бренд', 'Изображение карты'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['brand'], item['card_img']])


def parse():
    PAGENATION = input('Укажите глубину вложенности: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            s_file(cards, CSV)
        print(f'Всего спаршено {len(cards)} карт')
    else:
        print('Error')


parse()
