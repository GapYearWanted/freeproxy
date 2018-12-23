# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class Ip3366Spider(RedisSpider):
    name = "ip3366"
    redis_key = "freeproxyspider:start_urls:ip3366"


    def start_requests(self):
        yield Request(url="http://www.ip3366.net/")


    def parse(self, response):
        for line_tag in response.css("tbody tr"):
            tds = line_tag.css("td::text").extract()
            host, port, proxy_type = tds[0], tds[1], tds[3]
            print(host, port, proxy_type)

