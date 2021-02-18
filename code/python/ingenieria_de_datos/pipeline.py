import logging
import subprocess
import datetime
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('Pipe Line'+__name__)
news_site_uid = ['eluniversal','elpais']


def run():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting to scrap the news papers')
    
    for site in news_site_uid:
        logger.info('Scraping {}'.format(site))
        subprocess.run(['python3','main.py',site],cwd='./scraper') #Ejecuto el scraper
        subprocess.run(['find','.','-name','{}*'.format(site),'-exec','mv','{}', #Lo muevo a carpeta de transform, donde lo voy a modficar con pandas
                        '../transform/{}_.csv'.format(site),';'],cwd = './scraper')


def _transform():
    logger.info('Starting to transform de data')
    now = datetime.datetime.now().strftime('%y_%m_%d')
    
    for site in news_site_uid:
        clean_file = '{}_{}.csv'.format(site,now)
        dirty_file = '{}_.csv'.format(site)

        subprocess.run(['python3','newspaper_receipe.py',dirty_file], cwd='./transform') #Ejecuto el script donde organizo el archivo csv
        subprocess.run(['rm',dirty_file] , cwd='./transform') #Borro el archivo viejo y sucio
        subprocess.run(['mv',clean_file,'../db_sql/{}.csv'.format(site)], cwd='./transform') #Muevo y renombro el nuevo archivo organizado 


def _load():
    logger.info('Starting load process')

    for site in news_site_uid:
        file = '{}.csv'.format(site)

        subprocess.run(['python3','main.py',file], cwd='./db_sql') #Ejecuto el archivo donde añado los datos a una bade de datsos en MySql
        subprocess.run(['rm', file ], cwd='./db_sql') #Elimino el archivo que me quedaba en formato csv


if __name__ == '__main__':
    run()