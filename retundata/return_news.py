import pymysql
class Renews():

    def __init__(self):
        self.db = pymysql.connect('localhost','root','Dwzx170322','graduate_design',charset = 'utf8')
        self.cursor = self.db.cursor()


    def fkrenews(self,num):
        sql = "SELECT * FROM `school_news` ORDER BY newno limit  %s,%s" % (
            num*10, 20)
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        listtable = []
        for row in results:
            item={}
            item['newid'] = row[1]
            item['newurl'] = row[2]
            item['newdate'] = row[3]
            item['newimpa'] = row[4]
            item['newtitle'] = row[5]
            listtable.append(item)
        table = {}
        table['data'] = listtable
        return table

# x=Renews()
# print(x.fkrenews(1))