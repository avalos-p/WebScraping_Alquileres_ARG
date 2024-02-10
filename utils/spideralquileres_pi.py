import scrapy
from config.cfg import PARAIRNOS_WEBSITE,PARAIRNOS_PROVINCES,PATH_CSV
import datetime

import logging

date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

class SpideralquileresSpider_PI(scrapy.Spider):
    name = "spideralquileres_PI"
    allowed_domains = PARAIRNOS_WEBSITE
    start_urls = list(PARAIRNOS_PROVINCES.values())
    

    custom_settings = {
    'FEED_FORMAT': 'csv',
    'FEED_URI': f'{PATH_CSV}/alquileres_pi{date_formatted}.csv'# saving raw data
    }
    

    def parse(self, response):
        houses = response.css('.card-horizontal') #this is the container for information

        for house in houses:
            yield{
                'name' : house.css('h4.title::text').get(),
                'price': house.xpath('.//span[@class="price "]/text()[3]').get().replace('.', ';'),
                'days': house.css('div.price-sub::text').get(),
                'rooms': house.css('ul.list-inline.amenities li::text').re_first(r'\d+').replace('.', ';'),
                'bathrooms': house.css('ul.list-inline.amenities li::text').re_first(r'\d+\s*Bañ[os]'),
                'capacity': house.css('ul.list-inline.amenities li::text').re_first(r'\d+\s*Persona[s]'),
                'date': date_formatted,
                'province': next((provincia for provincia, url in PARAIRNOS_PROVINCES.items() if provincia in response.url), None),
                'site':'parairnos.com',
                }


        next_page_list = response.css('ul.pagination li a::attr(href)')
        next_page = next_page_list[-1]


        if next_page:
            if next_page == self.start_urls[0]:
                pass
            else:
                yield response.follow(next_page, callback=self.parse)

