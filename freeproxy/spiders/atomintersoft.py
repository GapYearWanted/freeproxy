# coding:utf8

import scrapy
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class AtomintersoftSpider(scrapy.Spider):
    name = "atomintersoft"
    redis_key = "freeproxyspider:start_urls:freeproxylist"
    GFW = True
    start_urls = ["http://www.atomintersoft.com/anonymous_proxy_list"]


    def parse(self, response):
        for tr_tag in response.css("tr"):
            tds = tr_tag.css("td::text").extract()
            proxy = tds[0]
            print(proxy)

