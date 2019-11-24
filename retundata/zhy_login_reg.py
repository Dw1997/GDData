import pymysql

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
        sql = "select * from orderlist where %s=%s and getpost=%s"%(who,userphone,gp)
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


dw = ZHY_Login_Reg()
re = dw.orders('getuser','10000',0)
print(re)
# re2 = dw.register('zhy_3','dw','12345a','6单元405')
# dw = Login_Reg()
# re = dw.check('18930913829','123')
# print(re)
# re2 = dw.register('15579760328','dw','dwsdsghh@163.com','Dwzx5201314')
# print(re2)
# re3 = dw.check('15579760328',hashlib.md5('Dwzx5201314'.encode('utf8')).hexdigest())
# print(re3)

