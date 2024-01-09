import scrapy
from config.cfg import ARGENPROP_WEBSITE,ARGENPROP_PROVINCES,PATH_CSV
import datetime

import logging

date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

class SpideralquileresSpider_AP(scrapy.Spider):
    name = "spideralquileres_AP"
    allowed_domains = ARGENPROP_WEBSITE # calling sites from cfg 
    start_urls = list(ARGENPROP_PROVINCES.values()) #
    
    custom_settings = {
    'FEED_FORMAT': 'csv',
    'FEED_URI': f'{PATH_CSV}/alquileres_ap{date_formatted}.csv' # saving raw data
    }
    

    def parse(self, response):
        houses = response.css('.listing__item') #this is the container for information

        for house in houses:
            yield{
                'name' : house.css('.card__address::text').get(),
                'price': house.xpath('.//p[@class="card__price"]/text()[2]').get(),
                'days': 'not available',
                'rooms': house.css('li:has(i.icono-cantidad_dormitorios) span::text').get(),
                'bathrooms': house.css('li:has(i.icono-cantidad_banos) span::text').get(),
                'capacity': 'not available',
                'date': date_formatted,
                'province': next((provincia for provincia, url in ARGENPROP_PROVINCES.items() if provincia in response.url), None),
                'site':'argenprop.com',
                }


        
        next_page =self.allowed_domains[0]+response.css('a[aria-label="Siguiente"]::attr(href)').get()


        if next_page:
            if next_page == self.start_urls[0]:
                pass
            else:
                yield response.follow(next_page, callback=self.parse)
 # TO DO: solve captcha
















































