# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Games_Infos_Item(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    rating = scrapy.Field()
    favorites = scrapy.Field()
    published = scrapy.Field()
    categories = scrapy.Field()
    developer = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    picture = scrapy.Field()

class Games_Link_Item(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()
    picture = scrapy.Field()