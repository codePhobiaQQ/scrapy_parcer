import scrapy
import xlsxwriter

OUT_XLSX_FILENAME = "out.xlsx"

class InnovationSpider(scrapy.Spider):
    name = 'innovation'
    allowed_domains = ['innovation-aks.ru']
    start_urls = ['https://innovation-aks.ru/']
    page_count = 1
    # header_row = 0
    
    
    # def dump_to_xlsx(filename, item):
    #     with xlsxwriter.Workbook(filename) as workbook:
    #         ws = workbook.add_worksheet()
    #         if (header_row == 0):
    #             bold = workbook.add_format({'bold': True})
    #             headers = ['url', 'title', 'price']
    #             for col, h in enumerate(headers):
    #                 ws.write_string(0, col, h, cell_fomat=bold)
    #             header_row = 1
    #             return
    #         else:
    #             for row, item in enumerate(item):
    #                 ws.write_string(row, 0, item['url'])
    #                 ws.write_string(row, 1, item['title'])
    #                 ws.write_string(row, 2, item['price'])
    # dump_to_xlsx(OUT_XLSX_FILENAME, "")
    
    
    def start_requests(self):
        print("startstartstartstartstartstartstartstartstartstartstartstartstartstartstart")
        for page in range(1, 1 + self.page_count): 
            url = f'https://innovation-aks.ru/category/chekhly_1/?page={page}'
            yield scrapy.Request(url, callback=self.parce_pages)
            

    def parce_pages(self, response, **kwargs):
        for href in response.css('.catalog__item .catalog__item__title a::attr("href")').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)
            
            
    def parse(self, response, **kwargs):        
        print(response.css("h1 span::text").extract_first().encode().decode().strip())
        item = {
            'url': response.request.url,
            'title': response.css("h1 span::text").extract_first().strip(),
            'price': response.css(".product__block .price::text").extract_first().strip(),
        }
        return item
        # return dump_to_xlsx(OUT_XLSX_FILENAME, item)
