# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class MrhinkydinkSpider(RedisSpider):
    name = "mrhinkydink"
    redis_key = "freeproxyspider:start_urls:mrhinkydink"


    def start_requests(self):
        yield Request(url="http://www.mrhinkydink.com/proxies.htm")


    def parse(self, response):
        #print(response.text)
        print(response.css("tr.text"))
        for line_tag in response.css("tr.text")[:-1]:
            tds = line_tag.css("td::text").extract()
            host, port = tds[0], tds[1]
            print(host, port)

