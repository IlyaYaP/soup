import json
from urllib import response
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
import time
from random import randrange
import re
import os
from itertools import chain

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
    # with requests.Session() as session:
    #     for page in range(1, pagination_count + 1):
    #         print(page)

    #         response = session.get(url=f'https://neiros.ru/blog/analytics/?page={page}', headers=headers, verify=False)
            
    #         soup = BeautifulSoup(response.text, 'lxml')
    #         articles_url = soup.find_all('a', class_='icon-right')



    #         for au in articles_url:
    #             art_url = 'https://neiros.ru' + au.get('href')
    #             article_url_list.append(art_url)
    #         time.sleep(randrange(2, 5))
    #         print(f'Обработал {page}/{pagination_count}')
    
    #     with open('articles_urls.txt', 'w') as file:
    #         for url in article_url_list:
    #             file.write(f'{url}\n')

    #     return 'Работа по сборy ссылок выполнеан'

def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]

    with requests.Session() as session:
        result_data = []

        for url in urls_list[:1]:
            response = session.get(url=url, headers=headers, verify=False)
            soup = BeautifulSoup(response.text, 'lxml')
            article_title = soup.find('div', class_='article-home-wrapper').find('h1', class_='aticle-h1').text
            article_author = soup.find('div', class_='author-article').find('a').text
            article_pub_date = soup.find('div', class_='article-home-box').find('p').text
            #post_section = [post_section.text.strip().replace('\n', ' ') for post_section in soup.find('div', class_='entry-content').find_all('section')]
            count=0
            result_data.append({
                'Название статьи': article_title,
                'Автор статьи': article_author,
                'Дата публикации': article_pub_date,
                # 'Пост': post_section_1,
                # 'img': article_img_tags
            })
            for post_section in soup.find('div', class_='entry-content').find_all('section'):
                h2 = post_section.find('h2').text

                h3 = [h3.text.strip().replace('\n', ' ') for h3 in post_section.find_all('h3')]


                li = post_section.find_all('li')
                li = [li.text.strip().replace('\n', ' ') for li in li]
                for lis in li:
                    if h3 is not result_data:

                

                        result_data.append({h2: lis})
                


            # article_img =  soup.find('div', class_='entry-content').find_all('img')
            # article_img_tags = ['https://neiros.ru' + img['src'] for img in article_img]
            

# Загрузка медиа в папку data_img/{article_title}

            # for url in article_img_tags:
            #     newpath = fr'C:\Users\Оля\Dev\soup\data_img\{article_title}' 
            #     if not os.path.exists(newpath):
            #         os.makedirs(newpath)
            #     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
            #     if not filename:
            #         print("Regex didn't match with the url: {}".format(url))
            #         continue
            #     with open(f'data_img/{article_title}/{filename.group(1)}', 'wb') as f:
            #         if 'http' not in url: 
            #             url = '{}{}'.format(url)
            #         response = session.get(url=url, headers=headers, verify=False)
            #         f.write(response.content)

    
    with open(f'data_1.json', 'w', encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)



    # with open('data/index_2.html', 'w') as file:
    #     file.write(response.text)


def main():
    # print(get_articles_urls(url='https://neiros.ru/blog/analytics/'))
    get_data('articles_urls.txt')


if __name__ == '__main__':
    main()


