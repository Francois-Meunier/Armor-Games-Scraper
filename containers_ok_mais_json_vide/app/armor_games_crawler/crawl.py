import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.spyder_Armor_Games import  ArmorGamesSpider
from spiders.spyder_games_infos import  ArmorGamesSpider1

FEED_URI1 = "jeux.json"
FEED_URI2 = "jeux_infos.json"
FEED_FORMAT = "json"

def scrap_games_link():
    # CrawlerProcess
    process = CrawlerProcess({'FEED_URI':FEED_URI1, 'FEED_FORMAT':FEED_FORMAT})  # Init the crawl
    process.crawl(ArmorGamesSpider)
    process.start(stop_after_crawl=True)

    return "scrap_link done"

def scrap_games_infos():
    # CrawlerProcess
    process = CrawlerProcess({'FEED_URI':FEED_URI2, 'FEED_FORMAT':FEED_FORMAT})  # Init the crawl
    process.crawl(ArmorGamesSpider1)
    process.start(stop_after_crawl=True)

    return "scrap_infos done"
