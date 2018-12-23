# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class KuaidailiSpider(RedisSpider):
    name = "kuaidaili"
    redis_key = "freeproxyspider:start_urls:kuaidaili"


    def start_requests(self):
        yield Request(url="https://www.kuaidaili.com/free/inha/")


    def parse(self, response):
        for line_tag in response.css("tbody tr"):
            tds = line_tag.css("td::text").extract()
            host, port, proxy_type = tds[0], tds[1], tds[3]
            print(host, port, proxy_type)

