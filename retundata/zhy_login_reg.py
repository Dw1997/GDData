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
        sql = "select userpass,usertype from user where userphone='%s'"%user
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            spass = results[0][0]
        except:
            spass = None

        self.db.close()

        # if hashlib.md5(spass.encode('utf8')).hexdigest()==passw:
        if spass == passw:
            return results[0][1]
        else:
            return False

    def register(self,userphone,username,userpass,useraddr):
        sql = "insert into user values ('%s','%s','%s','%s','%s')"%(userphone,username,userpass,1,useraddr)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result


# dw = ZHY_Login_Reg()
# re = dw.check('18930913829','123')
# print(re)
# re2 = dw.register('zhy_3','dw','12345a','6单元405')
# print(re2)
# re3 = dw.check('15579760328',hashlib.md5('Dwzx5201314'.encode('utf8')).hexdigest())
# print(re3)

