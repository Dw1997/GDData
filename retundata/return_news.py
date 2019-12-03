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
                        dict(zip(['num', 'id', 'url', 'date','year','month','day', 'impa', 'title', 'state'], list(n))))
                # print(listn)
        except:
            # print(listr)
            self.db.rollback()
            # print(sql)
        return listr

    def newsearch(self,typee,inf):
        year1='0'
        month='0'
        day='0'
        if typee=='1':
            searchitem='newtitle'
            item = '%'
            for i in range(len(inf)):
                item = item+inf[i]
            item = item+'%'
            sql = "select * from `school_news` where newtitle like '%s'"%item
        if typee=='2':
            longi = len(inf)
            #时间中有. 例如2019.1.1 1.1
            if '.' in inf:
                hh = inf.split('.')
                if len(hh)==3:
                    year = hh[0]
                    if len(year)==4:
                        year1=year
                    if len(year)==2:
                        year1='20'+year
                    month = hh[1]
                    day = hh[2]
                if len(hh)==2:
                    month = hh[0]
                    day = hh[1]
            # 时间中有 ' '，例如2019 10 9，10 9
            elif ' ' in inf:
                hh = inf.split(' ')
                if len(hh) == 3:
                    year = hh[0]
                    if len(year) == 4:
                        year1 = year
                    if len(year) == 2:
                        year1 = '20'+year
                    month = hh[1]
                    day = hh[2]
                if len(hh) == 2:
                    month = hh[0]
                    day = hh[1]
            # 时间中有'/'，例如2019/10/9 10/9
            elif '/' in inf:
                hh = inf.split('/')
                if len(hh) == 3:
                    year = hh[0]
                    if len(year) == 4:
                        year1 = year
                    if len(year) == 2:
                        year1 = '20'+year
                    month = hh[1]
                    day = hh[2]
                if len(hh) == 2:
                    month = hh[0]
                    day = hh[1]

            elif ' ' not in inf and '/' not in inf and ' ' not in inf:
                year1='2019'
                if len(inf)==8:
                    year1 = inf[0:4]
                    month = inf[4:6]
                    day = inf[6:]
                if len(inf)==6:
                    if inf[0:2]=='20':
                        year1 = inf[0:4]
                        month = inf[4:]
                    else:
                        year1=inf[0:2]
                        month=inf[2:4]
                        day = inf[4:]
                if len(inf)==4:
                    if inf[0:2]=='20':
                        year1 = inf[0:4]
                        month = inf[4:]
                    else:
                        month=inf[0:2]
                        day=inf[2:]
                if len(inf)==2:
                    month = inf[0:1]
                    day = inf[1:2]
                if len(inf)==3:
                    if inf[1]>'3':
                        month=inf[0:2]
                        day=inf[2]
                    else:
                        month=inf[0]
                        day=inf[1:]

            print(year1,month,day)
            if month!='0' and day!='0' and year1!='0':
                sql = "select * from `school_news` where newmonth='%s' and newday='%s' and newyear='%s'"%(month,day,year1)
            elif month!='0' and year1!='0':
                sql = "select * from `school_news` where newmonth='%s' and newyear='%s'"%(month,year1)
            elif month!='0' and year1!='0':
                sql = "select * from `school_news` where newmonth='%s' and newday='%s'"%(month, day)
            else:
                item = '%'
                for i in range(len(inf)):
                    item = item+inf[i]
                item = item+'%'
                sql = "select * from `school_news` where newdate like '%s'"%item
        
        print(sql)
        result = False
        listr = []
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                print(i)
                listr.append(
                    dict(zip(['num', 'id', 'url', 'date', 'year', 'month', 'day', 'impa', 'title', 'state'], list(i))))
        except:
            print('error')
            result=False
        return listr



x = Renews()
x.newsearch('2','201910')
# x.addlog('1','1')
# print(datetime.datetime.now())
