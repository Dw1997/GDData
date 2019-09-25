# -*- coding: utf-8 -*-
import scrapy
from jqnews.items import JqnewsItem


class JqsnewsSpider(scrapy.Spider):
    name = 'jqsnews'
    allowed_domains = ['news.gench.edu.cn']
    start_urls = ['https://news.gench.edu.cn/2090/list.htm',
                  'https://news.gench.edu.cn/2088/list.htm',
                  'https://news.gench.edu.cn/2089/list.htm']
                  # 'https://news.gench.edu.cn/2096/list.htm',
                  # 'https://news.gench.edu.cn/2094/list.htm',
                  # 'https://news.gench.edu.cn/2120/list.htm'

    def parse(self, response):
        res = response.xpath('//ul[@class = "wp_article_list"]/li/div[@class = "fields pr_fields"]/span[@class = "Article_Title"]/a/@href').extract()
        for i in res:
            self.log(i)
            url = 'https://news.gench.edu.cn'+i
            yield scrapy.Request(url,callback=self.getitem,dont_filter=True)
        nextpage = 'https://news.gench.edu.cn'+response.xpath('//li[@class = "page_nav"]/a[@class = "next"]/@href').extract_first()
        yield scrapy.Request(nextpage,callback=self.parse,dont_filter=True)

    def getitem(self,response):
        item = JqnewsItem()
        item['newurl'] = response.url
        item['newid'] = item['newurl'].split('/')[-2]
        item['newtitle'] = response.xpath('//div[@class = "article"]/h1[@class = "arti_title"]/text()').extract_first()
        item['newdate'] = response.xpath('//p[@class = "arti_metas"]/span[@class = "arti_update"]/text()').extract_first().split(':')[-1]
        try:
            item['newimpa'] = 'https://news.gench.edu.cn' + response.xpath('//img/@src').extract_first()
            # item['newimpa'] = 'https://news.gench.edu.cn'+response.xpath('//div[@class = "read"]/div[@class = "wp_articlecontent"]/p/img/@src').extract_first()
        except TypeError:
            print("error")
            # item['newimpa'] = 'https://news.gench.edu.cn' + response.xpath('//div[@class = "imgnav imgnav1"]/div[@class = "img"]/img/@src').extract_first()
        # if item['newimpa'] == None:
        #     item['newimpa'] = 'https://news.gench.edu.cn' + response.xpath('//div[@class = "read"]/div[@class = "wp_articlecontent"]/div/div/divimg/@src').extract_first()
        # if item['newimpa'] ==None:
        #     item['newimpa'] = 'https://news.gench.edu.cn' + response.xpath('//div')
        yield item

