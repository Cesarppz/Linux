from bs4 import BeautifulSoup
import requests 
import urllib

def run():
    for i in range(2405,2411):
        response = requests.get(f'https://xkcd.com/{i}')
        soup = BeautifulSoup(response.content,'html.parser')
        image_container = soup.find(id='comic')

        image_url  = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Decargando ...')
        urllib.request.urlretrieve(f'https:{image_url}',image_name)

if __name__ == '__main__':
    run()