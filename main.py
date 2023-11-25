import scrapy
from scrapy.crawler import CrawlerProcess
from spideralquileres_ap import SpideralquileresSpider_AP
from spideralquileres_pi import SpideralquileresSpider_PI

def run_spiders():
    process = CrawlerProcess()
    process.crawl(SpideralquileresSpider_AP)
    process.crawl(SpideralquileresSpider_PI)
    process.start()

if __name__ == "__main__":
    run_spiders()



