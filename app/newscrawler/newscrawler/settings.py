# -*- coding: utf-8 -*-

# Scrapy settings for newscrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newscrawler'

SPIDER_MODULES = ['newscrawler.spiders']
NEWSPIDER_MODULE = 'newscrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newscrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False 


CONCURRENT_REQUESTS_PER_DOMAIN = 100

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 50,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 100
}


ROTATING_PROXY_LIST_PATH = '../data/proxies.txt'

USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
]

#faire transiter les items par les pipelines pour traiter les strings scrapper

ITEM_PIPELINES = {
     'newscrawler.pipelines.PublishedPipeline': 100,
     'newscrawler.pipelines.NamePipeline' : 200,
     'newscrawler.pipelines.RatingsPipeline': 300,
     'newscrawler.pipelines.FavoritesPipeline': 400,
     'newscrawler.pipelines.PlaysPipeline' : 500,
     'newscrawler.pipelines.MongoPipeline': 600
 }