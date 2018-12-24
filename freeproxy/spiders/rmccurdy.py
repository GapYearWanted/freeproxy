# coding:utf8

import scrapy
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class RmccurdySpider(scrapy.Spider):
    name = "rmccurdy"
    start_urls = ["https://www.rmccurdy.com/scripts/proxy/good.txt"]

    def parse(self, response):
        for proxy in response.text.strip().split("\n"):
            print(proxy)

