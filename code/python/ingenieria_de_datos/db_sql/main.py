from article import Article
from base import Base, engine, Session
import pandas as pd 

import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('news paper data base'+__name__)


def main(file_name):
    Base.metadata.create_all(engine) #Crear el esquema
    session = Session()              #Inicializo la sesion 
    articles = pd.read_csv(file_name)

    for idx, row  in articles.iterrows():
        logger.info('Loading article number {} with uid {} into a DB'.format(idx,row['uid']))
        article = Article(row['uid'],
                          row['body'],
                          row['title'],
                          row['url'],
                          row['host'],
                          row['num_title'],
                          row['num_body'],
                          row['uid_site']
                            )
        session.add(article)
    session.commit()
    session.close()
        


        



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',
                        help='Put the file that you want to convert uin a data base',
                        type=str)
    args = parser.parse_args()
    
    main(args.file_name)