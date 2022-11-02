from asyncore import write
import json
from urllib import response
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
import time
from random import randrange
import re
import os
import csv


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


headers = {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


# Сбор url в файл articles_url.txt

def get_articles_urls(url):
    with requests.Session() as session:
        response = session.get(url=url, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('ul', class_ = 'pagination').find_all('a', class_='page-link')[-2].text)

    article_url_list = []
    with requests.Session() as session:
        for page in range(1, pagination_count + 1):
            print(page)

            response = session.get(url=f'https://neiros.ru/blog/analytics/?page={page}', headers=headers, verify=False)
            
            soup = BeautifulSoup(response.text, 'lxml')
            articles_url = soup.find_all('a', class_='icon-right')



            for au in articles_url:
                art_url = 'https://neiros.ru' + au.get('href')
                article_url_list.append(art_url)
            time.sleep(randrange(2, 5))
            print(f'Обработал {page}/{pagination_count}')
    
        with open('articles_urls.txt', 'w') as file:
            for url in article_url_list:
                file.write(f'{url}\n')

        return 'Работа по сборy ссылок выполнеан'



def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]

    with requests.Session() as session:
        

        for url in urls_list[:1]:
            response = session.get(url=url, headers=headers, verify=False)
            soup = BeautifulSoup(response.text, 'lxml')
            
            article_title = soup.find('div', class_='article-home-wrapper').find('h1', class_='aticle-h1').text

            

            h2 = [post_section.find_all(['h2', 'h3']) for post_section in soup.find('div', class_='entry-content').find_all('section')]
            for i in h2:
                if len(i)<=1:
                    i 


                else:
                    i


            result_data = [article_title]

            
                    



            



            # for i in h2:

            #     h2_ = [h2.text.strip().replace('\n', ' ') for h2 in i]




            #     result_data.append(h2_)


            # h3 = [h3.text for h3 in soup.find('div', class_='entry-content').find_all('h3')]

    
            with open(f'data.json', 'w', encoding="utf-8") as file:
                json.dump(result_data, file, indent=6, ensure_ascii=False)



    # with open('data/index_2.html', 'w') as file:
    #     file.write(response.text)


def main():
    # print(get_articles_urls(url='https://neiros.ru/blog/analytics/'))
    get_data('articles_urls.txt')


if __name__ == '__main__':
    main()


