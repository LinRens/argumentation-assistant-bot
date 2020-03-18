# парсер заголовков и текста с сайта https://new-science.ru/svet-eto-chastica-ili-volna/
# выбор1: или при нажатии кнопкки "хочу статью" выдается выбор категорий:
# общие знания, знаменитые ученые, химия, физика, технологии, спелеология, софт, робототехника,
#психология, природа, палеонтология, здоровье и медицина, моя планета, математика, космонавтика, история,
# искусственный интеллект, интернет, геология, гаджеты, биология, астрономия, археология, антропология
# добавить кнопки на выбор
# https://new-science.ru/category/obshhie-znaniya/
# при выборе кнопки моделируется ссылка на рубрику
# со странички рубрики парсится список ссылок на ссответствующие статьи + краткие описания+ картинка (?)
# функция get_article(url, category)
# словарь или список? содержит: ссылка, заголовок, краткое описание, ссылка на картинку?
# список из N статей, N - лимит одной страницы. на каждой кнопке написано сколько статей осталось
import requests
from bs4 import BeautifulSoup

category = 'obshhie-znaniya' #будет определяться в запросе обработчика сообщений
url = 'https://new-science.ru/category/' + category

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
# прописать функцию def get_head(url):
everything = soup.find_all('div', {'class': 'post-details'})
what = []
# РАБОТАЕТ НЕ ТРОГАТЬ
texts = soup.find_all('p', {'class': 'post-excerpt'})
title = soup.find_all('h2', {'class': 'post-title'})
href = soup.find_all('a', {'class': 'more-link button'})

for i in range(len(texts)):
    print(title[i].string)
    print(texts[i].string)
    print(href[i].get('href'))
    print()
