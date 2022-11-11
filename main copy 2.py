import json
from urllib import response
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
import time
from random import randrange
import re
import os

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


headers = {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

url = 'https://ria.ru/world/'
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

def get_first_news():
    article_card = soup.find_all('div', class_ = 'list-item')
    new_list = {}
    for article in article_card:
        article_data = article.find('div', class_ = 'list-item__date').text
        article_title = article.find('a', class_ = 'list-item__title color-font-hover-only').text
        article_href = article.find('a', class_ = 'list-item__title color-font-hover-only').get('href')
        
        article_id = article_href.split('/')[-1]
        article_id = article_id[:-5]
        new_list[article_id] = {
            'article_data': article_data,
            'article_title': article_title,
            'article_href': article_href
        }

    with open('new_list.json', 'w', encoding="utf-8") as file:
        json.dump(new_list, file, indent=4, ensure_ascii=False)


def main():
    get_first_news()

if __name__ == '__main__':
    main()