
from email.policy import default
from bs4 import BeautifulSoup
import requests
import json
import csv

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# r = requests.get("url", params={"key_1": "value_1", "key_N": "value_N"}, verify=False)
# Код запроса

url = 'https://neiros.ru/blog/business/kto-takoy-kontragent-i-chem-otlichaetsya-ot-klienta/'
headers = {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers, verify=False)
src = req.text

# Сохраняем страницу локально

# with open('index.html', 'w') as file:
#     file.write(src)

# Читаем наш сохраненный файл и сохраняем его в переменную, далее вытаскиваем нужные ссылки и сохраняем в json формате

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

try:
    list_section =[]
    list_item =[]

    name_post = soup.find('div', class_='article-home-wrapper').find('h1').text
    post_body = soup.find('div', class_='entry-content')
    post_description = post_body.find('p').text
    # sections = [sections.text for sections in post_body.find_all('section')] 

    sections = soup.find('a', class_='links-toggle links-blue').find_next()
    section = [section.text for section in sections]
    # item = [item.text.strip() for item in sections.find_all('p',)]
    # item_ul = [item_ul.text for item_ul in sections.find_all('ul')]
    list_section.append({
            'name_post': name_post,
            'post_description': post_description,
            'section': section
            })

    with open('list_section.json', 'w') as file:
        json.dump(list_section, file, indent=4, ensure_ascii=False)



    # list_section.append({
    #         'body_post': sections.find('p')
    #     })



    # with open('list_section.json', 'a') as file:
    #     json.dump(list_section, file, indent=4, ensure_ascii=False)


    with open(f"data/1.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(list_section)

except Exception as ex:
    print(ex)



