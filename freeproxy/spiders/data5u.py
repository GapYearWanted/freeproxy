# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class Data5uSpider(RedisSpider):
    name = "data5u"
    redis_key = "freeproxyspider:start_urls:data5u"


    def start_requests(self):
        yield Request(url="http://www.data5u.com/free/index.shtml")


    def parse(self, response):
        for line_tag in response.css(".l2"):
            spans = line_tag.css("span li::text").extract()
            host, port, proxy_type = spans[0], spans[1], spans[3]
            print(host, port, proxy_type)

