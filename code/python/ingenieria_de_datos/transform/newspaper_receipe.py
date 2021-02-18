import logging
from urllib.parse import urlparse
import argparse
import pandas as pd
import datetime
import hashlib
import re
import nltk 
from nltk.corpus import stopwords


file_name_dir = re.compile(r'\w+\/\w+.csv$')


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('news paper wraggling'+__name__)


def main(file_name):
    log.info('Starting to cleaning the data')
    df  = _read_db(file_name)
    site_id = _extract_name(file_name)
    df = _add_newspaper_colum_id(df,site_id)
    df = _parser_url_column(df)
    df = _fill_missing_titles(df)
    df = _create_hash(df)
    df = _replace_caracters(df)
    df = _num_of_token(df, 'title')
    df = _num_of_token(df, 'body')
    df = _drop_row_duplicates_entries(df,'title')
    df = _drop_row_with_missing_values(df) 
    _save_newdb(df,site_id)
    return df


def _read_db(file_name):
    log.info('Start reading the data base')
    return pd.read_csv(file_name,encoding='utf-8')


def _extract_name(file_name):
    log.info('name detected, starting to extract the data')
    site_id = file_name.split('_')[0]
    site_id_dir = re.match(file_name_dir,file_name)
    if site_id_dir:
        site_id = site_id.split('/')[1]  
    log.info(f'the site id is {site_id}')
    return site_id


def _add_newspaper_colum_id(df,site_id):
    log.info('Starting to crate the site id ({}) column'.format(site_id))
    df['uid_site'] = site_id
    return df  


def _parser_url_column(df):
    log.info('Starting to create the url parse column')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)
    return df


def _fill_missing_titles(df):
    log.info('Filling missing titles')
    mask = df['title'].isna()
    missing_titles = (df[mask]['url'].str  #De los datos faltantes dados por la mask , le saco las urls 
                               .extract(r'(?P<url_title>[^/]+)$') #Extraigo el titulo de la url
                               .applymap(lambda x : x.split('-')) #Divido por los - que los separa
                               .applymap(lambda x : ' '.join(x)) #Uno con espacios 
                     )
    df.loc[mask,'title'] = missing_titles['url_title']
    return df 


def _create_hash(df):
    log.info('Creating index hash')
    uid = (df['url'].apply(lambda row : hashlib.md5(bytes(row.encode())))
                    .apply(lambda hash_object: hash_object.hexdigest() ) #Cambio el objeto hash a hexadecimal 
           )
    df['uid'] = uid
    df = df.set_index('uid')
    return df 


def _replace_caracters(df):
    log.info('Replacing of countless characters')
    stripped_body = df['body'].apply(lambda row : re.sub(r'[xa0|{|}|\\n]+','',row))
    df['body'] = stripped_body
    return df 
 


def _save_newdb(df,site_id):
    log.info('Saving the new file')
    now = datetime.datetime.now().strftime('%y_%m_%d')
    name = '{}_{}.csv'.format(site_id,now)
    df.to_csv(name)
    

def _drop_row_duplicates_entries(df,column_name):
    df.drop_duplicates(subset=[column_name],keep='first',inplace=True)
    return df 


def _drop_row_with_missing_values(df):
    return df.dropna()


def token(token_column,file_name):
    df = main(file_name)
    df = _num_of_token(df,token_column)
    site_id = _extract_name(file_name)
    _save_newdb(df,site_id)
    

def _num_of_token(df, name_column):
    log.info('Start to craeting the tokens')
    stop_words = set(stopwords.words('spanish'))  #Creo un set con las stop words que son paralbras como la, el. Que no suman valor 

    num_token = (df
            .dropna()
            .apply(lambda row : nltk.word_tokenize(row[name_column]),axis = 1) #Creo los token, que son las palabras
            .apply(lambda tokens : list(filter(lambda word: word.isalpha(),tokens)))# Filtro todas las a
            .apply(lambda tokens : list(map(lambda word:word.lower(), tokens))) #Coloco todas en minúscula para que se puedan comparar con la lista de stops words 
            .apply(lambda tokens : list(filter(lambda word: word not in stop_words , tokens)))#Filtro palabras quenno esten en las stop words
            .apply(lambda tokens : len(tokens))
           )
    df['num_'+ name_column] = num_token
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_name',
        help='Put the path to clean the dirty data base',
        type=str)
    parser.add_argument('token',
                        help='Put the name of the column that you want to count the numbers tokens',
                        type=str,
                        nargs='?')

    args = parser.parse_args()
    
    main(args.file_name)
    if args.token:
        token(args.token,args.file_name)
    
