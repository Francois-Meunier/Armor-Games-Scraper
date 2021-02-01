import scrapy
from scrapy import Request
import json

class ArmorGamesSpider(scrapy.Spider):
    name = "url_scrapper"
    start_urls = ["https://armorgames.com/games/date/1#games",]



    def parse(self, response):
        for ele in response.xpath('//ul[@class="gamelisting"]/li'):
            name = ele.xpath('h5/a/text()').extract_first()
            rating = ele.xpath('p[@class="rating"]/text()').extract_first()
            plays = ele.xpath('p[@class="plays"]/text()').extract_first()
            liens_url = ele.xpath('a/@href').extract_first()
            image  = ele.xpath('a/img/@src').extract_first()
            yield { 
                    'name' : name ,
                    'rating' : rating[8:],
                    'plays' : plays, 
                    'lien url' : "https://armorgames.com"+liens_url,
                    'image' : image
                    }
        next_urls = ["/games/date/"+str(i)+"#games" for i in range(2,int(response.xpath('//div[@class="pagination"]/a/text()').extract()[-2])+1) ]           
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse)

            