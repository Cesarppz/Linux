import requests
import lxml.html as html # para aplicar xpahth a html 
import datetime 
import os 


LINK='https://www.larepublica.co/'
XPAHT_LINK_TO_ARTICLE= '//text-fill[not(@class)]/a/@href'
XPAHT_TITLE= '//div[@class="mb-auto"]/text-fill[not(@class)]/a[@class="economiaSect"]/text()'
XPAHT_RESUME= '//div[@class="news economiaSect"]/div[@class="lead"]/p/text()'
XPAHT_ARTICLE = '//*[contains(concat( " ", @class, " " ), concat( " ", "html-content", " " ))]/p/text()'

def parse_notice(link,today):
    try:
        response= requests.get(link)
        
        if response.status_code == 200:
            notice= response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            
            try:
                title = parsed.xpath(XPAHT_TITLE)[0] #pongo el indice 0 porque solo quiero el primer item de la lista
                title= title.replace('\"','')      
                summary = parsed.xpath(XPAHT_RESUME)[0]
                article = parsed.xpath(XPAHT_ARTICLE)

            except IndexError:
                return
            
            with open('{}/{}.txt'.format(today,'h'),'w',encoding='utf-8') as f: 
                f.write(title)             # el with es un manejador contextual que se usa en este caso por si hay un error no vaya a corromper la carpeta
                f.write('\n\n')            # En el with el primer parámetro es un nomnbre o una ruta 
                f.write(summary)
                f.write('\n\n')  
                for p in article:
                    f.write(p)
                    f.write('\n\n')
        else:
            raise ValueError(f'Error {response.status_code}') 
    
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(LINK) #Traer el html de la página
        if response.status_code == 200:
            home= response.content.decode('utf-8')#Para que el archivo no tenga problemas con caracteres como la ñ
            parsed = html.fromstring(home)   # tomar el archivo html de home y convetirlo para poder manejarlo con path
            link_to_notices= parsed.xpath('//h2/a/@href')
            #print(link_to_notices) 

            today = datetime.date.today().strftime('%d-%m-%y') # Medir la fecha de hoy y convertirlo en formato string para poder nombrar la carpeta
            
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in link_to_notices:
                    parse_notice(link,today)
        else:
            raise ValueError(f'Error {response.status_code}')

    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__== '__main__':
    run()
   