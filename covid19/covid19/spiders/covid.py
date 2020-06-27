# -*- coding: utf-8 -*-
import scrapy
from covid19.items import Covid19Item

class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.bbc.com/news/world-51235105']
    start_urls = ['https://www.bbc.com/news/world-51235105/']

    def parse(self, response):
        item = Covid19Item()
        values_converted = []
        item['countrie'] = [x.strip() for x in response.css("table.core tbody tr.core__row  td.core__region::text").getall()]

        values = [x.strip() for x in   response.css("table.core tbody tr.core__row  td.core__value::text").getall()]
        [values_converted.append(int( x.replace(",","") if x != "" else 0)) for x in values]
        item['values'] = values_converted
        yield item