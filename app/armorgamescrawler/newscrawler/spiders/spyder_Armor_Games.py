import scrapy
from scrapy import Request
import json
from ..items import Games_Link_Item

class ArmorGamesSpider(scrapy.Spider):
    name = "url_scrapper"
    start_urls = ["https://armorgames.com/games/date/1#games",]
    custom_settings = {
            'ITEM_PIPELINES' : {
                }
        }



    def parse(self, response):
        for ele in response.xpath('//ul[@class="gamelisting"]/li'):
            name = ele.xpath('h5/a/text()').extract_first()
            rating = ele.xpath('p[@class="rating"]/text()').extract_first()
            plays = ele.xpath('p[@class="plays"]/text()').extract_first()
            link = ele.xpath('a/@href').extract_first()
            picture  = ele.xpath('a/img/@src').extract_first()


            yield Games_Link_Item(
                    name = name ,
                    rating = rating[8:],
                    plays = plays, 
                    link = "https://armorgames.com"+link,
                    picture = picture
            )


        next_urls = ["/games/date/"+str(i)+"#games" for i in range(2,int(response.xpath('//div[@class="pagination"]/a/text()').extract()[-2])+1) ]           
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse)

            