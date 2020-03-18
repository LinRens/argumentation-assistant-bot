import requests
from bs4 import BeautifulSoup

category = 'obshhie-znaniya' #будет определяться в запросе обработчика сообщений
url = 'https://new-science.ru/category/'


def get_news(url, category):
    link = url + category
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")

    texts = soup.find_all('p', {'class': 'post-excerpt'})
    title = soup.find_all('h2', {'class': 'post-title'})
    href = soup.find_all('a', {'class': 'more-link button'})

    news = []

    for i in range(len(texts)):
        news.append('*' + title[i].string + '*')
        news[i] += '\n' + texts[i].string + '\n' + href[i].get('href')
    return news
