from config.cfg import PATH_LOGS,PATH_CSV,LOG_TASKS,LOG_CFG

import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime



from utils.spideralquileres_ap import SpideralquileresSpider_AP
from utils.spideralquileres_pi import SpideralquileresSpider_PI
from utils.logger import create_logger_from_file, get_logger
from utils.utils import *
from utils.cleaning import *

create_logger_from_file(LOG_CFG) # Logger from .conf file.
logger = get_logger(LOG_TASKS) # Logger name 


date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

def run_spiders():
    logger.info('Starting scraping.')
    process = CrawlerProcess()
    process.crawl(SpideralquileresSpider_AP)
    process.crawl(SpideralquileresSpider_PI)
    process.start()

if __name__ == "__main__":
    # Running spiders
    run_spiders()

    # Code for cleaning
    argenprop_data = pd.read_csv(f'{PATH_CSV}/alquileres_ap{date_formatted}.csv')
    argenprop_data = data_cleaner(argenprop_data)
    
    parairnos_data = pd.read_csv(f'{PATH_CSV}/alquileres_pi{date_formatted}.csv')
    parairnos_data = data_cleaner(parairnos_data)

    results = append_data(argenprop_data, parairnos_data)

    # Database connection
    logger.info('Connecting to db.')
    engine = connection_db()
    logger.info('Uploading Data.')
    upload_db(f'alquileres_clean{date_formatted}',engine)
