import scrapy
import json
import time
from ..items import games_info_item
from scrapy import Request

with open('data/jeux.json')  as json_file:
    data = json.load(json_file)
    urls = []
    for games in data:
        urls.append(games['link'])

class ArmorGamesSpider1(scrapy.Spider):
    name = "jeux_infos_scrapper"
    allowed_domains =['armorgames.com']
    start_urls = urls
    custom_settings = {
            "DOWNLOAD_DELAY" : 0.1, 
            "HTTPCACHE_ENABLED" : True, 
            "CONCURRENT_REQUESTS_PER_IP" : 300,
            "ROBOTSTXT_OBEY" : True,
            'ITEM_PIPELINES':{
                'armor_games_crawler.pipelines.PublishedPipeline': 100,
                'armor_games_crawler.pipelines.NamePipeline' : 200,
                'armor_games_crawler.pipelines.RatingsPipeline': 300,
                'armor_games_crawler.pipelines.FavoritesPipeline': 400,
                'armor_games_crawler.pipelines.PlaysPipeline' : 500,
                'armor_games_crawler.pipelines.MongoPipeline': 600
            }

        }

    def parse(self, response):
            name = response.css(".game-header.clearfix h1::text").extract_first()[1:]
            info_value = response.css("#description-tab .stats .value::text").extract()
            categories = response.css(".categories .tag-category::text").extract()
            developer = response.css(".bio a::attr(href)").extract_first()
            description = response.css("#description p::text").extract_first()
            for i in data:
                if i["name"] == name[:-1] :
                    link = i["link"]
                    picture = i["picture"]
            

            yield games_info_item(
                        name = name,
                        plays = info_value[0],
                        ratings = info_value[1],
                        favorites = info_value[2],
                        published = info_value[3][1:],
                        categories = categories,
                        developer = developer,
                        description = description,
                        link = link,
                        picture = picture
            )