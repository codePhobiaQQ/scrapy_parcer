import requests
from bs4 import BeautifulSoup as BS
import scrapy

link = "https://innovation-aks.ru/category/chekhly_1/"

request = requests.get(link)
html = BS(request.content, 'html.parser')

for el in html.select(".catalog__item > .catalog__item__block"):
    title = el.select(".catalog__item__title > a")
    print(title[0].text)