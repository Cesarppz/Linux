from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PractSpider(CrawlSpider):
    name = 'practica'
    start_urls = ['https://books.toscrape.com/']
    allowed_domains = ['books.toscrape.com']
    base_url = 'https://books.toscrape.com/'
    
    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI':'resultados.csv',
        'MEMUSAGE_LIMIT_MB':200000

    }


    rules = [
        Rule(LinkExtractor(allow=r'/page')),
        Rule(LinkExtractor(allow=r'index.html'),callback='parser')
       
    ]

    # rules =  [Rule(LinkExtractor(allow=r'/catalogue'),callback='parser,follow=True)]


    def parser(self,response):
        if response.xpath('//article[@class="product_page"]/p/text()').get():

            title = response.xpath('/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1/text()').get()
            price = response.xpath('/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[3]/td/text()').get()
            description = response.xpath('//article[@class="product_page"]/p/text()').get()
            

            yield {
                'title':title,
                'price':price,
                'description':description
            }
        else:
            print(response.url)