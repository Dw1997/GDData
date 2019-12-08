import pymysql
import math
import random
import datetime

class ZHY_Login_Reg():

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Dwzx170322'
        self.port = 3306
        self.dbname = 'zhy'
        self.db = pymysql.connect(self.host, self.user, self.password, self.dbname, charset='utf8')
        self.cursor = self.db.cursor()
        

    def check(self,user,passw):
        sql = "select * from user where userphone='%s'"%user
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            spass = results[0][2]
        except:
            spass = None

        self.db.close()

        # if hashlib.md5(spass.encode('utf8')).hexdigest()==passw:
        if spass == passw:
            lista = []
            for i in results[0]:
                lista.append(i)
            ret = dict(zip(['phone','name','paas','type','addr','area'],lista))
            return ret
        else:
            return False

    def register(self,userphone,username,userpass,useraddr,areaid):
        sql = "insert into user values ('%s','%s','%s','%s','%s','%s')"%(userphone,username,userpass,1,useraddr,areaid)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result

    def addposter(self,userphone,username,userpass,areaid):
        sql = "insert into user values ('%s','%s','%s','%s','%s','%s')"%(userphone,username,userpass,'2','小区物业',areaid)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result

    def changepass(self,userphone,userpass,usernew):
        sql = "select userpass from user where userphone=%s"%userphone
        print(sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            oldpass = result[0][0]
            if oldpass==userpass:
                sql = "update user set userpass=%s where userphone=%s"%(usernew,userphone)
                self.cursor.execute(sql)
                self.db.commit()
                res = True
            else:
                res = False
        except:
            self.db.rollback()
            res = False

        return res

    def orders(self,who,userphone,gp):
        if who=='getuser':
            sql = "select * from orderlist where %s=%s and getpost=%s"%(who,userphone,gp)
        if who=='poster':
            sql = "select * from orderlist where %s=%s and getpost=%s and state=0" % (
                who, userphone, gp)
        print(sql)
        listo = []
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                dicts = dict(zip(['orderid','getuser','poster','state','getpost','timee'],list(i)))
                listo.append(dicts)
            # print(listo)
            res = listo
        except:
            self.db.rollback()
            res = False
        return res
    
    def poster_send(self, phone, addr, areaid):
        sql = "select userphone from user where useraddr='%s' and areaid='%s' "%(addr,areaid)
        orderid = str(math.floor(1e7 * random.random()))
        data = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time()).split('.')[0]
        time1 = data+' '+time
        lista = []
        ret = False
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                print(i[0])
                lista.append(i[0])
            for d in lista:
                sqld = "insert into `orderlist` values ('%s','%s','%s','%s','%s','%s')"%(orderid,d,phone,'0','1',time1)
                print(sqld)
                self.cursor.execute(sqld)
                self.db.commit()
            ret = True
        except:
            ret = False
            self.db.rollback()
        return ret
    
    def user_send(self,uphone,gname,gphone,gaddr):
        sql = "select username,useraddr,areaid from `user` where userphone=%s"%uphone
        id = str(math.floor(1e7 * random.random()))
        data = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time()).split('.')[0]
        time1 = data+' '+time
        ret = False
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            name = res[0][0]
            uaddr = res[0][1]
            areaid = res[0][2]
            print(name,uaddr)
            sqld = "insert into `sendlist` values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,name,uphone,areaid,uaddr,gname,gphone,gaddr,time1,'0','0','0')
            print(sqld)
            self.cursor.execute(sqld)
            self.db.commit()
            ret = True
        except:
            self.db.rollback() 
        return ret
    
    def return_out(self,phone):
        '''
        用户获取发送到外面的快递
        '''
        sql = "select * from sendlist where uphone=%s"%phone
        listr = []
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                listr.append(dict(zip(['id','uname','uphone','areaid','uaddr','gname','gphone','gaddr','time','state','poster','kuaidid'],list(i))))
            print(listr)
        except:
            self.db.rollback()
        return listr

    def return_out_all(self,areaid):
        '''
        快递员获取发送到小区外的快递
        '''
        sql = "select * from sendlist where state=0 and areaid=%s"%areaid
        listr = []
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                listr.append(dict(zip(['id', 'uname', 'uphone', 'areaid', 'uaddr',
                                       'gname', 'gphone', 'gaddr', 'time', 'state','poster','kuaidid'], list(i))))
            print(listr)
        except:
            self.db.rollback()
        return listr
    
    def return_per(self,typee,areaid):
        '''
        获取小区内所有用户，快递员
        '''
        listr = []
        sql = "select * from user where usertype=%s and areaid=%s"%(typee,areaid)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                listr.append(dict(zip(['userphone','username','userpass','usertype','useraddr','areaid'],list(i))))
            print(listr)
        except:
            self.db.rollback()
        return listr
    
    def return_inf_n_a(self,utype,uphone):
        '''
        返回园区内用户地址或者快递员名字
        '''
        if utype=='1':
            sql = "select username from `user` where userphone=%s"%uphone
        if utype=='2':
            sql = "select useraddr from `user` where userphone=%s"%uphone
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            result =res[0][0]
            print(res,result)
        except:
            print(sql)
        return result
    
    def return_user(self,uphone):
        '''
        根据手机号获取用户信息
        '''
        sql = "select * from user where userphone=%s"%uphone
        dicta = {}
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            print(res)
            dicta = dict(zip(['userphone', 'username', 'userpass',
                               'usertype', 'useraddr', 'areaid'], list(res[0])))
        except:
            self.db.rollback()
            print(sql)
        return dicta

    def poser_get_it(self,itid,poser):
        '''
        快递员到家取快递时，跟新数据库
        '''
        sql = "UPDATE `sendlist` SET state='1',poster='%s' WHERE id='%s'"%(poser,itid)
        print(sql)
        result = False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            result = False
            self.db.rollback()
        return result
    
    def add_comment(self,id,up,pp,co):
        '''
        用户给快递订单评论
        '''
        result = False
        data = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time()).split('.')[0]
        time1 = data+' '+time
        sql = "insert into `comments` values ('%s','%s','%s','%s','%s')"%(id,up,pp,co,time1)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result

    def send_it(self,id):
        '''
        园区内快递确认送达、跟新数据库
        '''
        sql = "UPDATE `orderlist` SET state='1' WHERE orderids='%s'"%id
        print(sql)
        result = False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            result = False
            self.db.rollback()
        return result
    
    def get_out_poser(self,id):
        '''
        获取派件人员信息
        '''
        sql = "select poster,kuaidid from `sendlist` where id=%s"%id
        dicta = {}
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            print(res)
            poster = res[0][0]
            kuaidid = res[0][1]
            sqld = "select username from user where userphone=%s"%poster
            self.cursor.execute(sqld)
            resd = self.cursor.fetchall()
            print(resd)
            name = resd[0][0]
            dicta = dict(zip(['name','phone','kuaidid'],[name,poster,kuaidid]))
        except:
            self.db.rollback()
            print(sql,sqld)
        return dicta
    
    def get_out_orders(self,ph):
        sql = "select * from `sendlist` where poster=%s and state=1"%ph
        listr = []
        listr = []
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                listr.append(dict(zip(['id', 'uname', 'uphone', 'areaid', 'uaddr',
                                       'gname', 'gphone', 'gaddr', 'time', 'state', 'poster', 'kuaidid'], list(i))))
            print(listr)
        except:
            self.db.rollback()
        return listr

    def ins_out_kdi(self,id,kid):
        sql = "update `sendlist` set state='3',kuaidid=%s where id=%s"%(kid,id)
        result = False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result=True
        except:
            self.db.rollback()
            print(sql)
        return result
    
    def re_po_co(self,ph):
        listr = []
        sql = "select * from `comments` where poserphone='%s'"%ph
        try:
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for o in res:
                print(o)
                listr.append(
                    dict(zip(['id', 'user', 'poser', 'comm', 'time'], list(o))))
            print(listr)
        except:
            self.db.rollback()
        return listr

    def deluser(self,ph):
        result = False
        sql = "delete from `user` where userphone='%s'"%ph
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
        return result



dw = ZHY_Login_Reg()
x = dw.deluser('15579760328')
print(x)

# re2 = dw.register('zhy_3','dw','12345a','6单元405')
# dw = Login_Reg()
# re = dw.check('18930913829','123')
# print(re)
# re2 = dw.register('15579760328','dw','dwsdsghh@163.com','Dwzx5201314')
# print(re2)
# re3 = dw.check('15579760328',hashlib.md5('Dwzx5201314'.encode('utf8')).hexdigest())
# print(re3)
# getpost=1 快递员送 用户收
# getpost=0 快递员取 用户发


