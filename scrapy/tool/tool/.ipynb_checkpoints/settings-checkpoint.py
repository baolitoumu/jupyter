# -*- coding: utf-8 -*-

# Scrapy settings for tool project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
BOT_NAME = 'tool'
DEPTH_LIMIT=4
SPIDER_MODULES = ['tool.spiders']
NEWSPIDER_MODULE = 'tool.spiders'

##3
MYSQL_DB_NAME = 'scrapy_db'
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'new.1234'
# 
ITEM_PIPELINES = {
    'tool.pipelines.MySQLPipeline': 400,
}


CONCURRENT_REQUESTS_PER_IP = 2
COOKIES_DEBUG =True

DOWNLOADER_MIDDLEWARES = {
   #'tool.mymiddle.xianyumiddle.ProxyMiddleware': 100,
    'tool.mymiddle.RandomUserAgentMiddlware.RandomUserAgentMiddlware':100,
 #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
COOKIES_ENABLES = False



DBKWARGS={'db':'xianyu',"user":"root","passwd":"shashuai","host":"localhost","use_unicode":True,"charset":"utf8"}  

ua = UserAgent()

ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1
ua.ff
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
ua.safari
# Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25

# and the best one, random via real world browser usage statistic
ua.random


ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1
