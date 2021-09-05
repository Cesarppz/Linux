from datetime import datetime
import pytz 


if __name__ == '__main__':
    caracas_format = pytz.timezone('America/Caracas')
    my_datetime = datetime.now(caracas_format)
    date_format = my_datetime.strftime('%Y/%m/%d, %H:%M:%S')
    print('Carcas time:',date_format)


    bogota_format = pytz.timezone('America/Bogota')
    my_datetime = datetime.now(bogota_format)
    date_format = my_datetime.strftime('%Y/%m/%d, %H:%M:%S')
    print('Bogotá time:',date_format)
