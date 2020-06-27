# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    countrie = scrapy.Field()
    values = scrapy.Field()
    deaths = scrapy.Field()
    cases = scrapy.Field()
