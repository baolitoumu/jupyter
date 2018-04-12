# -*- coding: utf-8 -*-  
  
# Define your item pipelines here  
#  
# Don't forget to add your pipeline to the ITEM_PIPELINES setting  
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html  
  
import pymysql  
class MySQLPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        # 从项目的配置文件中读取相应的参数
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'scrapy_default')
        cls.HOST = crawler.settings.get("MYSQL_HOST", 'localhost')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'root')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", 'new.1234')
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)

        return item

    def insert_db(self, tx, item):
        values = (
                      item['numFound'],
            item['currPage'],
            item['totalPage'] ,
            item['ershouCount'],
            item['idleCount'] ,
            item['ershou'] ,
    
            item['user_Icon'],
            item['user_Nick'],
            item['user_vipLevel'] ,
            item['user_TypeId'] ,
            item['user_isTaobaoWomen'] ,
            item['user_taobaoWomenUrl'] ,
            item['user_CreditUrl'] ,
            item['user_ItemsUrl'],
            item['user_isSinaV'] ,
            item['user_yellowSeller'] ,
            
            item['item_imageUrl'] ,
            item['item_imageHeight'],
            item['item_imageWidth'] ,
            item['item_Url'] ,
            item['item_isBrandNew'] ,
            item['item_price'] ,
            item['item_orgPrice'] ,
            item['item_provcity'],
            item['item_describe'] ,
            item['item_publishTime'] ,
            item['item_From'] ,
            item['item_FromDesc'] ,
            item['item_FromTarget'] ,
            item['item_commentCount'] ,
            item['item_commentUrl'] ,
            item['item_collectCount'] ,
            item['item_title'],
        )
        sql = 'INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s)'
        tx.execute(sql, values)



