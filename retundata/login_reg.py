import pymysql

class Login_Reg():

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Dwzx170322'
        self.port = 3306
        self.dbname = 'graduate_design'
        self.db = pymysql.connect(
            self.host, self.user, self.password, self.dbname, charset='utf8')
        self.cursor = self.db.cursor()
        

    def check(self,user,passw):
        sql = "select * from user where userphone='%s'"%user
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            spass = results[0][3]
        except:
            spass = None

        self.db.close()

        # if hashlib.md5(spass.encode('utf8')).hexdigest()==passw:
        if spass == passw:
            lista = []
            for i in results[0]:
                lista.append(i)
            ret = dict(
                zip(['phone', 'name', 'mail', 'pass', 'type'], lista))
            return ret
        else:
            return False

    def register(self,userphone,username,usermail,userpass):
        sql = "insert into user values ('%s','%s','%s','%s','%s')"%(userphone,username,usermail,userpass,1)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            result = True
        except:
            self.db.rollback()
            result = False
        return result

    def changep(self,phone,oldp,newp):
        sql = "select userpass from user where userphone=%s"%phone
        # print(sql)
        result = False
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
            cpa = ret[0][0]
            print(cpa)
            if cpa==oldp:
                # print("密码正确")
                sql = "update user set userpass=%s where userphone=%s"%(newp,phone)
                print(sql)
                self.cursor.execute(sql)
                self.db.commit()
                result=True
            else:
                result=False
        except:
            self.db.rollback()
            result=False
        return result



# dw = Login_Reg()
# re = dw.changep('1000000','123','111')
# print(re)
# re2 = dw.register('15579760328','dw','dwsdsghh@163.com','Dwzx5201314')
# print(re2)
# re3 = dw.check('15579760328',hashlib.md5('Dwzx5201314'.encode('utf8')).hexdigest())
# print(re3)

