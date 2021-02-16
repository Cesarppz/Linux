import argparse
import datetime
import logging
from common import config
import news_pages_object as nw
import re 
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError
import csv


logging.basicConfig(level=logging.INFO)
loggin = logging.getLogger('The scraper '+__name__)

is_ok_link = re.compile(r'^https?://.+/.+$')
is_root = re.compile(r'^/.+$')


def _save_data(article,site_id):
    now = datetime.datetime.now().strftime('%y_%m_%d')   #Establesco el día, para colocarlo como nombre del archivo
    name_archive = '{}_{}_articles.csv'.format(site_id,now)
    csv_header = list(filter(lambda property : not property.startswith('_'), dir(article[2]))) #De los metodos que se puedes ejecutar (Que los obtengo con dir()) filtro todas las propiedades que no cominezan con _ , es decir me quedo con las propiedades que yo creé
    with open(name_archive,'w+',encoding='utf-8') as f:
        writter = csv.writer(f)
        writter.writerow(csv_header) #Escribo las cabezeras del archivo csv

        
        for article in article:
            row=[str(getattr(article,prop)) for prop in csv_header]
            writter.writerow(row)



def _build_link(host,link):             #Verifico los match de cada url, paera que tengan la direción completa 
    if re.match(is_ok_link,link):
        return link
    elif re.match(is_root,link):
        return '{}{}'.format(host,link)
    else:
        return '{}{}'.format(host,link)



def _fecth_article(site_id,host,link):   
    article = None

    try:
        article = nw.Pages(site_id,_build_link(host,link))    #Inicializo la clase para extraer info de la pg, pero antes verifico el link llamando la función _build_link
    except (HTTPError,MaxRetryError) :
        loggin.warning('Error while try fetching',exc_info=True)

    if article and not article.body :     
        loggin.warning('*'+'Error, the article has not body'+'*')
        return None

    else:
        return article


def _news_sites(site_id):                               
    host = config()['news_sites'][site_id]['url']  #Con el nombre que se pasó coo argumento, elijo el sitio, que tengo en el archivo yaml
    loggin.info(f'Beginning scraper for {host}')   #Creo un log info
    home_page = nw.NewsHomePages(site_id, host)    #Inicializo la clase de la pag principal 
    
    articles = []
    
    for idx,link in enumerate(home_page.article_links):  #Por cada link extraido de la pag principal 
        print(f'Scraping new number {idx} de {len(home_page.article_links)-1}')
        article = _fecth_article(site_id,host,link)  #LA funcioón donde extraigo la infomación de cada pag
        if article:
            loggin.info('Article fetched!!!')
            print(article.title)
            articles.append(article)
        #print('\n')
    print((len(articles)))

    _save_data(articles,site_id)
        

if __name__ == '__main__':
    news_choices = list(config()['news_sites'].keys())
    parser = argparse.ArgumentParser(description='News Scraper')  #Creo los argumentos 
    parser.add_argument(
        'news_site',
        type=str,
        help='Choice the news site that you want to scrap',
        choices=news_choices)

    args = parser.parse_args()
    _news_sites(args.news_site)   #Paso como site_id el nombre del argumento que se eligió. ES decir de los que estan en choices