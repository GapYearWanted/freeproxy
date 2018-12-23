# coding:utf8

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class P66ipSpider(RedisSpider):
    name = "66ip"
    redis_key = "freeproxyspider:start_urls:66ip"

    def start_requests(self):
        yield Request(url="http://www.66ip.cn/1.html",
                      headers={
                          "referer": "http://www.66ip.cn/1.html",
                          "host": "www.66ip.cn"
                      },
                      cookies={
                          "yd_cookie": "966c3c96-9274-42537c7e709bb1a2968357d900ffb0e61137",
                          "_ydclearance": "c322c6910399de9d7761c9f1-21ca-449a-a2c7-869552ccd3b8-1545565715"
                      })


    def parse(self, response):
        print(response.meta)
        for line_tag in response.css("#main tr")[1:]:
            tds = line_tag.css("td::text").extract()
            host, port = tds[0], tds[1]
            print(host, port)


# curl 'http://www.66ip.cn/1.html' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: http://www.66ip.cn/1.html' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: yd_cookie=966c3c96-9274-42537c7e709bb1a2968357d900ffb0e61137; _ydclearance=c322c6910399de9d7761c9f1-21ca-449a-a2c7-869552ccd3b8-1545565715'