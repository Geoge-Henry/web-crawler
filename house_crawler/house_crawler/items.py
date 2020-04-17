# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    house_name = scrapy.Field()
    # house_year = scrapy.Field()
    # house_type = scrapy.Field()
    # room_counts = scrapy.Field()
    # area = scrapy.Field()
    # location = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    total_price = scrapy.Field()
