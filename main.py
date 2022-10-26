import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


headers = {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}



def get_articles_urls(url):
    with requests.Session() as session:
        response = session.get(url=url, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('ul', class_ = 'pagination').find_all('a')[-1].text)
    print(pagination_count)

    # with open('data/index_2.html', 'w') as file:
    #     file.write(response.text)




def main():
    get_articles_urls(url='https://neiros.ru/blog/analytics/')



if __name__ == '__main__':
    main()


