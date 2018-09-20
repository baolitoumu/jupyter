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
    #_____________________url参数___________________________
        pn = 999
        pn = str(pn)
        usm='3'
        word='as2'
        sa='np'
        rsv_pq=''
        rsv_t=''
        rqid=''
        url = 'https://m.baidu.com/s?pn='+pn+'&usm='+usm+'&word='+word+'&sa='+sa+'&rsv_pq='+rsv_pq+'&rsv_t='+rsv_t+'&rqid='+rqid        
    #_____________________url参数___________________________     
        yield scrapy.Request(url=url,callback=self.get_all_page,dont_filter=True)

    def get_all_page(self):
        contant = response.body.decode('utf-8')
        pages = Selector(text=contant).xpath("//span[contains(text(),"第")]")
        
        page_num = re.findall(r"\d+\.?\d*", pages)[0]
        yield scrapy.Request(url=url,callback=self.get_all_page,dont_filter=True)
        items = []
        for i in range(pn)
            item = ProxyItem()
            original_site= "m.baidu.com"
            keyword = "免费代理"
             #_____________________url参数___________________________
            pn=i*10
                if i==0:
                    pn=1
            usm='3'
            word='as2'
            sa='np'
            rsv_pq=''
            rsv_t=''
            rqid=''
            url = 'https://m.baidu.com/s?pn='+pn+'&usm='+usm+'&word='+word+'&sa='+sa+'&rsv_pq='+rsv_pq+'&rsv_t='+rsv_t+'&rqid='+rqid
            item['search_url'] = url
            item['word'] = keyword
            items.append(item)
        for item in items:
             yield scrapy.Request(url=item['search_url'],meta={'item_0':item},callback=self.parse,dont_filter=True)
    


        