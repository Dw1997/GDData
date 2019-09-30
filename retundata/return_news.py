import pymysql
class Renews():

    def __init__(self):
        self.db = pymysql.connect('loaclhost','root','Dwzx170322','graduate_design',charset = 'utf8')
        self.cursor = self.db.cursor()

    def fkrenews(self,num):
        pass
