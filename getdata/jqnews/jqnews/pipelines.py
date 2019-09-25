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
    def from_scrapy(cls):
        return(

        )

    def start_spider(self,spider):
        self.db = pymysql.connect(host = self.host,user = self.user,password = self.password)
    def process_item(self, item, spider):
        return item
