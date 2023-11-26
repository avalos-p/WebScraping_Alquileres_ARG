import scrapy
from scrapy.crawler import CrawlerProcess
from spideralquileres_ap import SpideralquileresSpider_AP
from spideralquileres_pi import SpideralquileresSpider_PI

from utils.cleaning import *
import pandas as pd


def run_spiders():
    process = CrawlerProcess()
    process.crawl(SpideralquileresSpider_AP)
    process.crawl(SpideralquileresSpider_PI)
    process.start()

if __name__ == "__main__":
    # running spiders
    run_spiders()

    # code for cleaning
    file1 = pd.read_csv('csv/alquileres_ap25-11-2023.csv')
    file1 = data_cleaner(file1)
    
    file2 = pd.read_csv('csv/alquileres_25-11-2023.csv')
    file2 = data_cleaner(file2)

    newfile = append_data(file1, file2)


