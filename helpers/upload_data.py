import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime

from config.cfg import PATH_LOGS,LOG_TASKS,LOG_CFG,PATH_CSV,PATH_CLEARDATA

from utils.spideralquileres_ap import SpideralquileresSpider_AP
from utils.spideralquileres_pi import SpideralquileresSpider_PI
from utils.logger import create_logger_from_file, get_logger
from utils.utils import *
from utils.cleaning import *

#Some data wasn't upload correctly to db so I made this to upload a list of files to db
create_logger_from_file(LOG_CFG) # Logger from .conf file.
logger = get_logger(LOG_TASKS) # Logger name 

date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

lista_fechas = ['31-12-2023','01-01-2024','02-01-2024','03-01-2024','04-01-2024','05-01-2024','06-01-2024','07-01-2024','08-01-2024','09-01-2024']

logger.info('Connecting to db.')
engine = connection_db()


def appending_data(file1: pd.DataFrame,file2:pd.DataFrame,i) -> pd.DataFrame :
    if not isinstance(file1, pd.DataFrame) or not isinstance(file2, pd.DataFrame):
        raise ValueError('Error: Both files must be pandas DataFrames.')
    result = pd.concat([file1, file2], ignore_index=True)
    result.to_csv(f'{PATH_CLEARDATA}/alquileres_clean{i}.csv')
    return result # The idea is to apply this function using old structure



# Code for cleaning
for i in lista_fechas:

    print((f'{PATH_CSV}/alquileres_ap{i}.csv'))
    print((f'{PATH_CSV}/alquileres_pi{i}.csv'))
    print(f'alquileres_clean{i}')
    argenprop_data = pd.read_csv(f'{PATH_CSV}/alquileres_ap{i}.csv')
    argenprop_data = data_cleaner(argenprop_data)
    
    parairnos_data = pd.read_csv(f'{PATH_CSV}/alquileres_pi{i}.csv')
    parairnos_data = data_cleaner(parairnos_data)

    results = appending_data(argenprop_data, parairnos_data,i)
    logger.info('Uploading Data.')
    upload_db(f'{PATH_CLEARDATA}/alquileres_clean{i}.csv',engine)
