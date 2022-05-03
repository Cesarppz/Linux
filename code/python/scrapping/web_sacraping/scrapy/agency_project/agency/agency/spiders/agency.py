import scrapy 

# archivos = '//a[starts-with(@href,"collection") and (parent::h2|parent::h3)]/@href'
# h1 = '//h1[@class="documentFirstHeading"]/text()'
# paragraph = '//div[@class="field-item even"]/p[not(@class)]/text()'

class AgencySpider(scrapy.Spider):
    name            = 'agency'
    # custom_settings = {
    #     'FEEDS':{
    #         'agencua.csv':{
    #             'format': 'csv',
    #             'encoding': 'utf-8',
    #             'indent': 4,
    #             }
    #}}
    start_urls   = ['https://www.cia.gov/readingroom/historical-collections']




    custom_settings = {
        'FEED_URI':'agencia.csv',
        'FEDD_FORMAT':'csv',
        'FEED_EXPORT_ENCODING':'utf-8'
    }
    

    def parse(self,response):
        archives = response.xpath('//a[starts-with(@href,"collection") and (parent::h2|parent::h3)]/@href').getall()
        print('\n\n')
        print('-*-'*20)
        for link in archives:
            yield response.follow(link,callback=self.parse_archive,cb_kwargs={'link':response.urljoin(link)})

    def parse_archive(self,response,**kwargs):
        link      = kwargs['link']
        title     = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').get()

        yield {
            'link'     : link,
            'title'    :title,
            'paragraph':paragraph
        } 