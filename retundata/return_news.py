import pymysql
import datetime
class Renews():

    def __init__(self):
        self.db = pymysql.connect('localhost','root','Dwzx170322','graduate_design',charset = 'utf8')
        self.cursor = self.db.cursor()


    def fkrenews(self,num):
        sql = "SELECT * FROM `school_news` ORDER BY newno limit  %s,%s" % (
            num*10, 20)
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            listtable = []
            for row in results:
                dictn = dict(zip(['num','id','url','date','impa','title','state'],list(row)))
                listtable.append(dictn)
        except:
            self.db.rollback()
            print("something error")
        return listtable
    
    def addlog(self,newsid,user):
        date = datetime.datetime.now().date()
        tablename = str(date.year)+str(date.month)
        sql = "CREATE TABLE IF NOT EXISTS `%s` (newid varchar(20) NOT NULL,user varchar(20) default NULL,date varchar(28) default NULL);"%tablename
        # print(sql)
        try:
            self.cursor.execute(sql)
            sqld = "insert into `%s` values ('%s','%s','%s')" % (tablename,
                newsid, user, str(datetime.datetime.now()))
            self.cursor.execute(sqld)
            self.db.commit()
            result='true'
            # print(sqld)
        except:
            self.db.rollback()
            print("error")
            result='fail'
        # print(tablename)
        return result

# x=Renews()
# x.addlog('1','1')
# print(datetime.datetime.now())
