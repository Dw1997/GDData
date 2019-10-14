# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class JqnewsPipeline(object):
    def __init__(self,host,user,password,port,dbname):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.dbname = dbname

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get('HOST'),
            dbname = crawler.settings.get("DBNAME"),
            user = crawler.settings.get('USER'),
            password = crawler.settings.get('PASSWORD'),
            port = crawler.settings.get('PORT')
        )

    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.user,self.password,self.dbname,charset='utf8')
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = "insert into school_news values (0,'%s','%s','%s','%s','%s')"%(item['newid'],item['newurl'],item['newdate'],item['newimpa'],item['newtitle'])
        self.cursor.execute(sql)
        self.db.commit()
        return item
