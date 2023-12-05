import scrapy
from scrapy.crawler import CrawlerProcess
from spideralquileres_ap import SpideralquileresSpider_AP
from spideralquileres_pi import SpideralquileresSpider_PI


from config.cfg import PATH_LOGS,LOG_TASKS,LOG_CFG
from utils.logger import create_logger_from_file,get_logger
import pandas as pd

create_logger_from_file(LOG_CFG) # logger from .conf file
logger = get_logger(LOG_TASKS) # logger name 
from utils.cleaning import *

import datetime
date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

def run_spiders():
    logger.debug('Starting scraping.')
    process = CrawlerProcess()
    process.crawl(SpideralquileresSpider_AP)
    process.crawl(SpideralquileresSpider_PI)
    process.start()

if __name__ == "__main__":
    # running spiders
    run_spiders()

    # code for cleaning
    file1 = pd.read_csv(f'csv/alquileres_ap{date_formatted}.csv')
    file1 = data_cleaner(file1)
    
    file2 = pd.read_csv(f'csv/alquileres_pi{date_formatted}.csv')
    file2 = data_cleaner(file2)

    newfile = append_data(file1, file2)


