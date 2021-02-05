from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from armor_games_crawler.spiders.spyder_Armor_Games import ArmorGamesSpider
#from armor_games_crawler.spiders.spyder_games_infos import ArmorGamesSpider1
from pymongo import MongoClient

if __name__=='__main__':

    client = MongoClient('mongodb_project',27017)

    process = CrawlerProcess(get_project_settings())
    process.crawl(ArmorGamesSpider)
    #process.crawl(ArmorGamesSpider1)
    process.start()