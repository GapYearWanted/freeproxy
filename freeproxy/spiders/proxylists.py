# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class ProxylistsSpider(RedisSpider):
    name = "proxylists"
    redis_key = "freeproxyspider:start_urls:proxylists"


    def start_requests(self):
        yield Request(url="http://www.proxylists.net/http_highanon.txt")


    def parse(self, response):
        for proxy in response.text.strip().split("\n"):
            print(proxy)

