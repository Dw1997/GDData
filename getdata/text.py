import pymysql
dw = pymysql.connect('localhost','root','Dwzx170322','graduate_design',charset='utf8')
cr = dw.cursor()
sql = "insert into school_news values ('%s','%s','%s','%s','%s')"%('3333333','22222','3333333333','4444444444444','1111111111111111')
cr.execute(sql)
dw.commit()