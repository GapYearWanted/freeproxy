# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class Ab57Spider(RedisSpider):
    name = "ab57"
    redis_key = "freeproxyspider:start_urls:ab57"


    def start_requests(self):
        yield Request(url="http://ab57.ru/downloads/proxyold.txt")


    def parse(self, response):
        for proxy in response.text.strip().split("\n"):
            print(proxy)

