import requests
import json
import csv
from lxml import etree
import time
import pymysql

class News(object):
    def __init__(self):
        self.s = requests.session()
        self.urls = [
            'https://news.gench.edu.cn/2090/list.htm',
            'https://news.gench.edu.cn/2088/list.htm',
            'https://news.gench.edu.cn/2089/list.htm'
        ]
        self.writer = csv.writer(open('./getdata/news.csv','w',encoding='utf-8',newline=''))
        self.reader = csv.reader(open('./getdata/news.csv','r',encoding='utf-8'))
        self.db = pymysql.connect('localhost','root','Dwzx170322','graduate_design',charset='utf8')
        self.cursor = self.db.cursor()
    
    def get_one_news(self,url):
        time.sleep(2)
        newsurl = url
        newid = url.split('/')[-2]
        res = self.s.get(url, headers={'Connection': 'close'})
        html = etree.HTML(res.text)
        print(html)
        newstitle = html.xpath(
            '//div[@class = "article"]/h1[@class = "arti_title"]/text()')[0]
        newsdate = html.xpath(
            '//p[@class = "arti_metas"]/span[@class = "arti_update"]/text()')[0]
        try:
            newsimpa = 'https://news.gench.edu.cn' + html.xpath('//img/@src')[0]
        except:
            newsimpa = "hhhhh"

        print(newid, newstitle, newsurl, newsimpa, newsdate[5:])
        return newid, newstitle, newsurl, newsimpa, newsdate[5:]
    
    def get_one_html(self,typee,url):
        time.sleep(1)
        res = self.s.get(url, headers={'Connection': 'close'})
        html = etree.HTML(res.text)
        print(html)
        resu = html.xpath(
            '//ul[@class = "wp_article_list"]/li/div[@class = "fields pr_fields"]/span[@class = "Article_Title"]/a/@href')
        for i in resu:
            newsurl = 'http://news.gench.edu.cn'+i
            newsid, newstitle, newsurl, newsimpa, newdate = self.get_one_news(newsurl)
            self.writer.writerow([typee, newsid, newstitle, newsurl, newsimpa, newdate])

    def into_mysql(self):
        for i in self.reader:
            date = i[-1].split('-')
            year = date[0]
            month = date[1]
            day = date[2]
            idate = year+month+day
            sql = "insert into `news_new` values ('%s','%s','%s','%s','%s','%s','0')"%(i[1],i[0],i[2],i[3],i[4],idate)
            # self.cursor.execute
            try:
                self.cursor.execute(sql)
            except:
                print(sql)
                continue
        self.db.commit()

    def main(self):
        for typee,url in enumerate(self.urls):
            for i in range(1,2):
                url1 = url[:-4]
                url2 = url[-4:]
                urln = url1+str(i)+url2
                print(urln)
                try:
                    self.get_one_html(typee,urln)
                except:
                    continue
        self.into_mysql()

if __name__=='__main__':
    x = News()
    x.main()
    # x.into_mysql()
