# coding:utf8

import scrapy
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class FreeproxylistSpider(scrapy.Spider):
    name = "freeproxylist"
    redis_key = "freeproxyspider:start_urls:freeproxylist"
    GFW = True
    start_urls = ["https://www.us-proxy.org/", "https://www.socks-proxy.net/", "https://www.sslproxies.org/", "https://free-proxy-list.net/"]


    def parse(self, response):
        for tr_tag in response.css("tbody tr"):
            tds = tr_tag.css("td::text").extract()
            host, port = tds[0], tds[1]
            print(host, port)

