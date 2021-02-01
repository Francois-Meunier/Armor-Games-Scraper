# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ArticleItem(scrapy.Item):
    name = scrapy.Field()
    plays = scrapy.Field()
    ratings = scrapy.Field()
    favorites = scrapy.Field()
    published = scrapy.Field()
    categories = scrapy.Field()
    developer = scrapy.Field()
    description = scrapy.Field()