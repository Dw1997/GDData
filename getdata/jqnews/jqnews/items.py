# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    newid = scrapy.Field()
    newurl = scrapy.Field()
    newdate = scrapy.Field()
    newimpa = scrapy.Field()
    newtitle = scrapy.Field()
    pass
