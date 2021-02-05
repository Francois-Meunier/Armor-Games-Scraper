from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from armor_games_crawler.spiders.spyder_Armor_Games import ArmorGamesSpider
#from armor_games_crawler.spiders.spyder_games_infos import ArmorGamesSpider1
 
if __name__=='__main__':
 
    process = CrawlerProcess(get_project_settings())
    process.crawl(ArmorGamesSpider)
    #process.crawl(ArmorGamesSpider1)
    process.start()