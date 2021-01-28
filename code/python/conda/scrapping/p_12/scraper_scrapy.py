import scrapy 
from scrapy.crawler import CrawlerProcess


class Spider12(scrapy.Spider):
    name = 'spider12'
    # EStablesco los dominio donde quiero scarpear
    allowed_domains = ['pagina12.com.ar']
    
    custom_settings = {'FEED_FORMAT':'json',
                       'FEED_URI':'resultados.json',
                       'DEPTH_LIMIT':2,
                       'FEED_EXPORT_ENCODING' : 'utf-8'}
    
    # Las url de los articulos que quiero scraper , que los saco del anterior scraper con bs4
    
    start_urls = [
        'https://www.pagina12.com.ar/secciones/el-pais',
     'https://www.pagina12.com.ar/secciones/economia',
     'https://www.pagina12.com.ar/secciones/sociedad',
     'https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos',
     'https://www.pagina12.com.ar/secciones/deportes',
     'https://www.pagina12.com.ar/secciones/el-mundo',
     'https://www.pagina12.com.ar/secciones/cultura']
    
    def parse(self,response):
        
        news = response.xpath('//div[@class="article-box__container"]/h2/a/@href').getall()
        for new in news:
            yield response.follow(new, callback=self.parse_nota)
        
        
        
        # #Articulo 
        # nota_promocionada = response.xpath('//div[@class="article-box__container"]/h2/a/@href').getall()
        # #if nota_promocionada is not None:
        # print(nota_promocionada)
        # for nota in nota_promocionada:
        #         #pasar la respuesta a parse_nota
        #     yield response.follow(nota,callback=self.parse_nota)
            

        next_page = 'https://www.pagina12.com.ar{}'.format(response.xpath('//a[@class="pagination-btn-next"]/@href').get())
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


        # next_page = response.xpath('//div[@class="articles-list-pager"]/nav[@aria-label="Articles list pagination"]/a/@href')
        # if next_page is not None:
        #     next_page.follow(next_page,callback=self.parse)
        
    def parse_nota(self,response):
        
        title = response.xpath('//div[@class="article-titles"]//h1/text()').get()
        body = ' '.join(response.xpath('//div[@class="article-text"]/p/text()').getall())
        section = response.xpath('//div[@class="suplement"]/a/text()').get()
        yield {'section' : section,
                'url' : response.url,
                'title' : title,    
                'body' : body}
        
        
        
        # fecha
        # fecha_article = response.xpath('//span[@pubdate="pubdate"]/@datatime').get()
        # title = response.xpath('//div[@class="article-titles"]//h1/text()').get()
        # contenido
        # article_text = ''.join(response.xpath('//div[@class="article-text"]/text()').getall())
        # copete
        # copete_article = response.xpath('//div[@class="article-summary"]/text()').get()
        
        yield { 'url' : response.url,
                #'feha' : fecha_article,
                'title': title,
                'body' : article_text,
                'copete': copete_article}

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(Spider12)
    process.start()