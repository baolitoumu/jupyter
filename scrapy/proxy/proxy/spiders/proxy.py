import scrapy
from scrapy import Selector
from urllib import parse ， 
from scrapy.http import HtmlResponse
import json
import pdb
import re
import random
from proxy.items import ProxyItem 
from urllib.parse import quote
import re
import sys
sys.path.append(r"/opt/jupyter/scrapy/xianyu/xianyu/spiders/")

class example(scrapy.Spider):
   #下载城市链接
    name = "proxy"
    def start_requests():
        original_site= "m.baidu.com"
        keyword = "免费代理"
        pn = 999
        pn = str(pn)
        usm='3'
        word='as2'
        sa='np'
        rsv_pq=''
        rsv_t=''
        rqid=''
        url = 'https://m.baidu.com/s?pn='+pn+'&usm='+usm+'&word='+word+'&sa='+sa+'&rsv_pq='+rsv_pq+'&rsv_t='+rsv_t+'&rqid='+rqid
        
        yield scrapy.Request(url=url,callback=self.get_all_page,dont_filter=True)

    def get_all_page(self):
        contant = response.body.decode('utf-8')
        pages = Selector(text=contant).xpath("//span[contains(text(),"第")]")
        page_num = re.findall(r"\d+\.?\d*", pages)[0]
        items = []
        for i in range(page_num-1, -1,-1):
            item = ProxyItem()
            original_site= "m.baidu.com"
            #url参数
            keyword = "免费代理"

            pn=i*10
            if pn == 0:
                pn=1
            usm='3'
            word='as2'
            sa='np'
            rsv_pq=''
            rsv_t=''
            rqid=''
            url = 'https://m.baidu.com/s?pn='+pn+'&usm='+usm+'&word='+word+'&sa='+sa+'&rsv_pq='+rsv_pq+'&rsv_t='+rsv_t+'&rqid='+rqid
            #url参数
            item['search_url'] = url
            item['word'] = keyword
            item['page_num'] = page_num
            items.append(item)
        for item in items:
             yield scrapy.Request(url=item['search_url'],meta={'item_0':item},callback=self.get_detail_url,dont_filter=True)
                
    def get_detail_url(self):
        item_1= response.meta['item_0']
        item = XianyuItem()
        contant = response.body.decode('utf-8')
        items = []
        proxy_pages_url = Selector(text=contant).xpath("//div[@class='c-container']/a/@href")
        for i in proxy_pages_url:
            item['search_url'] = item_1['search_url']
            item['word'] = item_1['search_url']
            item['page_num'] = item_1['search_url']
            item['proxy_page_url'] = proxy_page_url
            items.append(item)
        for item in items：
            yield scrapy.Request(url=item['proxy_page_url'],meta={'item_0':item},callback=self.proxy_page_url,dont_filter=True)
    
        
        
    def proxy_page_url(self):
        item_1= response.meta['item_0']
        item = XianyuItem()
        contant = response.body.decode('utf-8')
        items = []