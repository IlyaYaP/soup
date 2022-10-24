
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

    name_post = soup.find('div', class_='article-home-wrapper').find('h1').text
    post_body = soup.find('div', class_='entry-content')
    post_description = post_body.find('p').text
    post_section = post_body.find('section')
    section = [section for section in post_body.find_all('section')]

    print(section)






except Exception as ex:
    print(ex)



