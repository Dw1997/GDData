import pymysql
def getnewid(cursor):
    sql = 'select newid from school_news'
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        yield i[0]


def update(cursor, newid, i):
    sql = "update school_news set newno=%s where newid='%s'"%(i,newid)
    print(sql)
    cursor.execute(sql)


if __name__ == "__main__":
    db = pymysql.connect('localhost', 'root', 'Dwzx170322',
                             'graduate_design', charset='utf8')
    cursor = db.cursor()
    a=0
    for i in getnewid(cursor):
        update(cursor,i,a)
        a+=1

    db.commit()

