import requests
from bs4 import BeautifulSoup
class getxs():

    def GETZY(self):
        ip = 'https://www.23us.so/files/article/html/13/13332/index.html'
        b = '.L'
        listli = []
        lista = []
        res = requests.get(ip)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        for news in soup.select(b):
            for i in range(0, len(news)):
                li = news.text
                a = news.select('a')[0]['href']
                listli.append(li)
                lista.append(a)
        return lista

    def GETZJID(self, list):
        listzjid = []
        for i in range(0, len(list)):
            zjid = (list[i].split('/')[-1].rsplit('.html'))[0]
            listzjid.append(zjid)
        return listzjid

    def GETBW(self, list):
        res1 = requests.get(list[-1])
        res1.encoding = 'utf-8'
        soup1 = BeautifulSoup(res1.text, 'html.parser')
        zj = soup1.select('h1')[0].text
        bw = soup1.select('#contents')[0].text
        return zj, bw

# item = getxs()
# a = item.GETZY()
# b = item.GETZJID(a)
# c,d = item.GETBW(a)
# print(c)
# print(d)
