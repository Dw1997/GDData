import pymysql
import hashlib

class Login_Reg():

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Dwzx170322'
        self.port = 3306
        self.dbname = 'graduate_design'

    def comnnect(self):
        self.db = pymysql.connect(self.host, self.user, self.password, self.dbname, charset='utf8')
        self.cursor = self.db.cursor()

    def check(self,user,passw):
        self.comnnect()
        sql = "select userpass from user where userphone='%s'"%user
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            spass = results[0][0]
        except:
            spass = None

        self.db.close()

        # if hashlib.md5(spass.encode('utf8')).hexdigest()==passw:
        if spass == passw:
            return True
        else:
            return False

    def register(self,userphone,username,usermail,userpass):
        self.comnnect()
        sql = "insert into user values ('%s','%s','%s','%s')"%(userphone,username,usermail,userpass)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result


# dw = Login_Reg()
# re = dw.check('18930913829',hashlib.md5('Dwzx170322'.encode('utf8')).hexdigest())
# print(re)
# re2 = dw.register('15579760328','dw','dwsdsghh@163.com','Dwzx5201314')
# print(re2)
# re3 = dw.check('15579760328',hashlib.md5('Dwzx5201314'.encode('utf8')).hexdigest())
# print(re3)

