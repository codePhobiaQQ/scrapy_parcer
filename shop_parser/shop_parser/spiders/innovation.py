import scrapy
import xlsxwriter
import pandas as pd

url_list = []
title_list = []
price_list = []
image_list = []
status_list = []

class InnovationSpider(scrapy.Spider):
    name = 'innovation'
    allowed_domains = ['innovation-aks.ru']
    start_urls = ['https://innovation-aks.ru/']
    page_count = 76
    current_page = 0
    
    def start_requests(self):
        for page in range(1, 1 + self.page_count): 
            self.current_page += 1
            url = f'https://innovation-aks.ru/category/chekhly_1/?page={page}'
            yield scrapy.Request(url, callback=self.parce_pages)
            

    def parce_pages(self, response, **kwargs):
        for href in response.css('.catalog__item .catalog__item__title a::attr("href")').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)
            
            
    def parse(self, response, **kwargs):        
        item = {   
            "url": response.request.url,
            "tilte": response.css("h1 span::text").extract_first().encode().decode().strip(),
            "price": response.css(".product__block .price::text").extract_first().strip(),
            "img": response.css(".product__photo .image a::attr('href')").extract_first().strip(),
            "status": response.css(".product-status::text").extract_first().strip()
        }
        
        url_list.append(response.request.url)
        title_list.append(response.css("h1 span::text").extract_first().encode().decode().strip())
        price_list.append(response.css(".product__block .price::text").extract_first().strip())
        image_list.append(response.css(".product__photo .image a::attr('href')").extract_first().strip())
        status_list.append(response.css(".product-status::text").extract_first().strip())
    
        df = pd.DataFrame({
            'Ссылка на товар': url_list,
            'Название товара': title_list,
            'Цена товара': price_list,
            'Ссылка на изображение товара': image_list,
            'Наличие': status_list,
        })
        # save in excel
        df.to_excel('innovation2.xlsx', index=False)
        
        yield item