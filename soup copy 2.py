from operator import index
from random import random
from time import sleep
from turtle import title
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
title = soup.find_all(class_='mzr-tc-group-item-href')

dict = []
count = 0
id = {'p0', 'p1', 'p2',}
try:
    for item in id:
        

        section_0 = soup.find('section', {'id': {item}})
        h2 = section_0.find('h2').text
        p = section_0.find_all('p')
        alt = section_0.find('figure').find('img').get('alt')
        src = 'https://neiros.ru/blog/business/kto-takoy-kontragent-i-chem-otlichaetsya-ot-klienta' + section_0.find('figure').find('img').get('src')
        ul = section_0.find('ul').text




        dict.append(
        {
            'h2': h2,
            'p1': p[1].text,
            'p2': p[2].text,

            'alt': alt,
            'src': src,
            'p4': p[4].text,
            'p5': p[5].text,
            'ul': ul.strip().split('\n')
        }
        )
except IndexError as error_msg:
    print(error_msg)


with open('dict.json', 'w') as file:
    json.dump(dict, file, indent=4, ensure_ascii=False)






# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#     #print(f'{item_text}: {item_href}')
#     all_categories_dict[item_text] = item_href

# with open('all_categories_dict.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# with open('all_categories_dict.json') as file:
#     all_categories = json.load(file)

# iteration_count = int(len(all_categories)) - 1 
# count = 0
# print(f"Всего итераций {iteration_count}")


# for category_name, category_href in all_categories.items():

#     rep = [',', ' ', '-', "'", "__"]
#     for item in rep:
#         if item in category_name:
#             category_name = category_name.replace(item, "_")

#     req = requests.get(url=category_href, headers=headers)
#     src = req.text

#     with open(f"data/{count}_{category_name}.html", 'w', encoding="utf-8") as file:
#         file.write(src)

#     with open(f"data/{count}_{category_name}.html", encoding="utf-8") as file:
#         src = file.read()

#     soup = BeautifulSoup(src, 'lxml')

#     #Проверка страницы на наличие страницы с продуктами
    
#     alert_block = soup.find(class_='uk-alert-danger')
#     if alert_block is not None:
#         continue

#     #Собираем заголовки страниц

#     table_head = soup.find(class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tr').find_all('th')
#     product = table_head[0].text
#     colories = table_head[1].text
#     proteins = table_head[2].text
#     fats = table_head[3].text
#     carbohydrates = table_head[4].text
    
#     with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 product,
#                 colories,
#                 proteins,
#                 fats,
#                 carbohydrates
#             )
#         )

#     #Собираем данные продуктов

#     products_data = soup.find(class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tbody').find_all('tr')

#     product_info = []

#     for item in products_data:
#         product_tds = item.find_all('td')

#         title = product_tds[0].find('a').text
#         colori = product_tds[1].text
#         proteins = product_tds[2].text
#         fats = product_tds[3].text
#         carbohydrates = product_tds[4].text

#         product_info.append(
#             {
#                 'title': title,
#                 'colori': colori,
#                 'proteins': proteins,
#                 'fats': fats,
#                 'carbohydrates': carbohydrates
#             }
#         )


#         with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     title,
#                     colori,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )
#             )
            

#     with open(f"data/{count}_{category_name}.json", "a", encoding="utf -8") as file:
#         json.dump(product_info, file, indent=4, ensure_ascii=False)

#     count +=1
#     print(f"Итераци {count}. {category_name} записан...")
#     iteration_count = iteration_count - 1

#     if iteration_count == 0:
#         print("Работа завершена")
#         break
#     print(f"Осталось итераций {iteration_count}")
