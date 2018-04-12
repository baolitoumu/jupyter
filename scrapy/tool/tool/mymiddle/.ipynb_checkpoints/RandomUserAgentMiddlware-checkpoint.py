#! -*- encoding:utf-8 -*-

import base64
from scrapy.http.cookies import CookieJar

proxyServer = "http-dyn.abuyun.com:9020"
proxyUser = "H73D894898XDG2VD"
proxyPass = "6902D1826CCEE2A5"
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

from fake_useragent import UserAgent
class RandomUserAgentMiddlware(object):

    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        #读取在settings文件中的配置，来决定ua采用哪个方法，默认是random，也可是ie、Firefox等等，参考前面的使用方法。
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    #更换用户代理逻辑在此方法中
    def process_request(self, request, spider):
        
        
        ua = UserAgent()

        
        request.headers.setdefault('User-Agent', ua.random)
        request.headers['User-Agent'] = ua.random
        #request.meta["proxy"] = proxyServer
        #request.headers["Proxy-Authorization"] = proxyAuth
        request.meta['proxy'] = "proxy.baibianip.com:8000"
        
        
        
        
       #request.headers.setdefault('cookie_jar', CookieJar())
        #request.meta["cookiejar"] = 'sadsad'
        
       # request.headers.setdefault('cookie', cookie())
        request.meta["cookie"] = None
      #  request.meta['proxy'] = "proxy.baibianip.com:8000"

