import pymysql
import datetime
class Renews():

    def __init__(self):
        self.db = pymysql.connect('localhost','root','Dwzx170322','graduate_design',charset = 'utf8')
        self.cursor = self.db.cursor()


    def fkrenews(self,num):
        '''
        返回新闻（旧）
        '''
        sql = "SELECT * FROM `school_news` ORDER BY newno limit  %s,%s" % (
            num*10, 20)
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            listtable = []
            for row in results:
                dictn = dict(zip(['num','id','url','date','year','month','day','impa','title','state'],list(row)))
                listtable.append(dictn)
        except:
            self.db.rollback()
            print("something error")
        return listtable
    
    def addlog(self,newsid,user):
        '''
        每月添加新闻点击量log
        '''
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

    def addlog2(self,newsid,user,idtp):
        '''
        用户收藏、赞、举报新闻
        '''
        date = datetime.datetime.now().date()
        tablename = str(date.year)+str(date.month)+'log'
        sql = "CREATE TABLE IF NOT EXISTS `%s` (newid varchar(20) NOT NULL,user varchar(20) default NULL,date varchar(28) default NULL,idtp varchar(1) default NULL);"%tablename
        result = False
        try:
            self.cursor.execute(sql)
            sqld = "insert into `%s` values ('%s','%s','%s','%s')" % (
                tablename, newsid, user, str(datetime.datetime.now()),idtp)
            self.cursor.execute(sqld)
            self.db.commit()
            result = 'true'
        except:
            self.db.rollback()
            result = False
        return result

    def rcogo(self,ty):
        '''
        返回用户收藏、点赞、举报新闻
        '''
        listr = []
        date = datetime.datetime.now().date()
        tablename = str(date.year)+str(date.month)+'log'
        sql = "select newid from `%s` where idtp='%s'"%(tablename,ty)
        try:
            listn = []
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                # print(i[0])
                listn.append(i[0])
            for d in listn:
                sqln = "select * from `news_new` where newsid='%s'" % d
                # print(sqln)
                self.cursor.execute(sqln)
                resn = self.cursor.fetchall()
                for n in resn:
                    listr.append(
                        dict(zip(['newsid', 'newstype', 'newstitle', 'newsurl', 'newsimpa', 'newsdate', 'newsstate'], list(n))))
                # print(listn)
        except:
            # print(listr)
            self.db.rollback()
            # print(sql)
        return listr
    
    def ruco(self,ph):
        '''
        返回用户收藏新闻
        '''
        listr = []
        date = datetime.datetime.now().date()
        tablename = str(date.year)+str(date.month)+'log'
        sql = "select * from `%s` where user='%s'"%(tablename,ph)
        try:
            listn = []
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                # print(i[0])
                listn.append(i[0])

            listb = list(set(listn))
            for d in listb:
                sqln = "select * from `news_new` where newsid='%s'" % d
                # print(sqln)
                self.cursor.execute(sqln)
                resn = self.cursor.fetchall()
                for n in resn:
                    listr.append(
                        dict(zip(['newsid', 'newstype', 'newstitle', 'newsurl', 'newsimpa', 'newsdate', 'newsstate'], list(n))))
                # print(listn)
        except:
            # print(listr)
            self.db.rollback()
            # print(sql)
        return listr

    
    def top20(self):
        '''
        返回本月点击最高新闻
        '''
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
                sqln = "select * from `news_new` where newsid='%s'" % d
                # print(sqln)
                self.cursor.execute(sqln)
                resn = self.cursor.fetchall()
                for n in resn:
                    listr.append(
                        dict(zip(['newsid', 'newstype', 'newstitle', 'newsurl','newsimpa','newsdate','newsstate'], list(n))))
                # print(listn)
        except:
            # print(listr)
            self.db.rollback()
            # print(sql)
        return listr

    def newsearch(self,typee,inf):
        '''
        搜索新闻
        '''
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
        return listr[:10]


    def deln(self,id):
        '''
        根据新闻id删除新闻
        '''
        sql = "delete from `news_new` where newsid='%s'"%id
        result = False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result=True
        except:
            self.db.rollback()
        return result

    def delcon(self,id,ph):
        '''
        取消收藏的新闻
        '''
        date = datetime.datetime.now().date()
        tablename = str(date.year)+str(date.month)+'log'
        sql = "delete from `%s` where newid='%s' and user='%s' and idtp='0'"%(tablename,id,ph)
        result = False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
        return result

    def re_news_n(self,typee,num):
        listn = []
        if typee==0:
            sql = "select * from `news_new` order by newsdate desc limit  %s,%s"%(num*10,20)
        else:
            sql = "select * from `news_new` where newstype='%s' order by newsdate desc limit  %s,%s" % (
                typee,num*10,20)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                dicts = dict(zip(['newsid','newstype','newstitle','newsurl','newsimpa','newsdate','newsstate'],list(i)))
                listn.append(dicts)
        
        except:
            print(sql)
        
        return listn




x = Renews()
d = x.re_news_n('0',1)
print(len(d))
# print(datetime.datetime.now())
