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

create_logger_from_file(LOG_CFG) # Logger from .conf file.
logger = get_logger(LOG_TASKS) # Logger name 


date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y") # Can change in the future

def run_spiders():
    # Running all my spiders at the same time
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
    upload_db(f'{PATH_CLEARDATA}/alquileres_clean{date_formatted}.csv',engine)
