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
    
    def top20(self):
        listr = []
        table = str(datetime.datetime.now().year) + \
            str(datetime.datetime.now().month)
        sql = "SELECT newid,count(*) FROM `%s` GROUP BY newid ORDER BY COUNT(1) DESC LIMIT 20" % table
        try:
            listn = []   
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                # print(i[0])
                listn.append(i[0])
            for d in listn:
                sqln = "select * from `school_news` where newid='%s'" % d
                # print(sqln)
                self.cursor.execute(sqln)
                resn = self.cursor.fetchall()
                for n in resn:
                    listr.append(
                        dict(zip(['num', 'id', 'url', 'date', 'impa', 'title', 'state'], list(n))))
                # print(listn)
        except:
            # print(listr)
            self.db.rollback()
            # print(sql)
        return listr


x = Renews()
listp = x.top20()
print(listp)
# x.addlog('1','1')
# print(datetime.datetime.now())
