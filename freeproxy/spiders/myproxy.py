# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class MyproxySpider(RedisSpider):
    name = "myproxy"
    redis_key = "freeproxyspider:start_urls:myproxy"
    GFW = True

    def start_requests(self):
        yield Request(url="https://www.my-proxy.com/free-proxy-list.html")


    def parse(self, response):
        context = response.css(".list::text").extract()
        print(context)
        context2 = response.css(".list .to-lock::text").extract()
        print(context2)
