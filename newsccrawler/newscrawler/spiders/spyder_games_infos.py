import scrapy
from scrapy import Request
import json
import time
from ..items import ArticleItem

with open('../data/jeux_urls.json')  as json_file:
    data = json.load(json_file)
    urls = []
    for games in data:
        urls.append(games['lien url'])

class ArmorGamesSpider1(scrapy.Spider):
    name = "jeux_infos_scrapper"
    allowed_domains =['armorgames.com']
    start_urls = urls
    custom_settings = {
            "DOWNLOAD_DELAY" : 1, 
            "HTTPCACHE_ENABLED" : True, 
            "CONCURRENT_REQUESTS_PER_IP" : 300,
            "ROBOTSTXT_OBEY" : True,
            "USER_AGENT" :  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

        }



    def parse(self, response):
            name = response.css(".game-header.clearfix h1::text").extract_first()[1:]
            info_value = response.css("#description-tab .stats .value::text").extract()
            categories = response.css(".categories .tag-category::text").extract()
            developer = response.css(".bio a::attr(href)").extract_first()
            description = response.css("#description p::text").extract_first()
            

            yield ArticleItem(
                        name = name,
                        plays = info_value[0],
                        ratings = info_value[1],
                        favorites = info_value[2],
                        published = info_value[3][1:],
                        categories = categories,
                        developer = developer,
                        description = description
            )

            

            
            