# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class Swei360Spider(RedisSpider):
    name = "swei360"
    redis_key = "freeproxyspider:start_urls:swei360"


    def start_requests(self):
        yield Request(url="http://www.swei360.com/")


    def parse(self, response):
        for line_tag in response.css("tr")[1:]:
            tds = line_tag.css("td::text").extract()
            host, port, proxy_type = tds[0].strip(), tds[1].strip(), tds[3].strip()
            print(host, port, proxy_type)

