# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class IphaiSpider(RedisSpider):
    name = "iphai"
    redis_key = "freeproxyspider:start_urls:iphai"


    def start_requests(self):
        yield Request(url="http://www.iphai.com/")


    def parse(self, response):
        for line_tag in response.css("tr")[1:]:
            tds = line_tag.css("td::text").extract()
            host, port, proxy_type = tds[0].strip(), tds[1].strip(), tds[3].strip()
            print(host, port, proxy_type)

