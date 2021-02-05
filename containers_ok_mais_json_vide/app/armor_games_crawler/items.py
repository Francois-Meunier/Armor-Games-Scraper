# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
    
class games_info_item(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    ratings = scrapy.Field()
    favorites = scrapy.Field()
    published = scrapy.Field()
    categories = scrapy.Field()
    developer = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    picture = scrapy.Field()
    
class games_link_item(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    ratings = scrapy.Field()
    link = scrapy.Field()
    picture = scrapy.Field()