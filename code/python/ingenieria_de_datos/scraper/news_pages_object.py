import requests
from bs4 import BeautifulSoup
from common import config

class NewsPages:                          #Clase padre, de una pag común
    def __init__(self, site_id , url ):
        self._site_id = site_id
        self._config = config()['news_sites'][site_id]
        self._query = self._config['query']
        self._html = None
        self._visit(url)

    def _visit(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            self._html = BeautifulSoup(response.text,'lxml')

    def _content(self,etq,type_attr,attr):
        return self._html.find_all(etq,attrs={type_attr:attr})

    def _content_unique(self,etq,type_attr,attr):
        return self._html.find(etq,attrs={type_attr:attr})


class Pages(NewsPages):                #Clase de un artículo
    def __init__(self,site_id,url):
        super().__init__(site_id,url)

    @property
    def body(self):
        links_list = []
        try:
            link = self._content_unique(self._query['body_etq'],self._query['body_attr_type'],self._query['body_attr'])
            if link:
                links_list.append(link)
        except Exception as e:
            print(e)
        
        if self._site_id == 'elpais':
            try:
                res = set(link.p.get_text() for link in links_list)
                return res
            except Exception as e:
                print('ERROR',e) 
        else:
            res = links_list[0].get_text().strip()
            return res
    @property
    def title(self):
        try:
            link = self._content_unique(self._query['title_etq'],self._query['title_attr_type'],self._query['title_attr'])
            return link.get_text().strip()
        except Exception as e:
            print(e)




class NewsHomePages(NewsPages):  #Clase de la pag principa, deonde extraigo los links para los artículos
    def __init__(self, site_id , url ):
        super().__init__(site_id,url)
        

    @property
    def article_links(self):
        links_list = []
        for link in self._content(self._query['article_link_etq'],self._query['article_link_attr_type'],self._query['article_link_attr']):
            if link:
                links_list.append(link)
        if self._site_id == 'elpais':
            return set(link.a.get('href') for link in links_list)

        else:
            return set(link.get('href') for link in links_list)



    
