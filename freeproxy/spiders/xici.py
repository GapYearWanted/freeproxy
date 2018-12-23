# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class XiciSpider(RedisSpider):
    name = "xici"
    redis_key = "freeproxyspider:start_urls:xici"

    def start_requests(self):
        for i in range(1, 2):
            yield Request(url=f"https://www.xicidaili.com/nn/{i}")


    def parse(self, response):
        for line_tag in response.css("tr")[1:]:
            print(line_tag)
            tds = line_tag.css("td::text").extract()
            print(tds)
            host, port, proxy_type = tds[0], tds[1], tds[5]
            print(host, port)