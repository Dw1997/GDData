import pymongo
import pymysql

class getinform():
	def __init__(self):
		self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
		self.mydb = self.myclient['12306']
		self.mycol = self.mydb['cartable']
		self.sqldb = pymysql.connect("localhost", "root", "Dwzx5201314",
                         "12306timetable", charset="utf8")
		self.cursor = self.sqldb.cursor()

	def gettrain(self, head):
		item = self.mycol.find({"station_train_code": head})
		return item[0]

	def gettimetable(self, head):
		sql = "select * from "+head
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		listtable = []
		for row in results:
			item = {}
			item['arrive_day_diff'] = row[0]
			item['arrive_time'] = row[1]
			item['running_time'] = row[2]
			item['start_time'] = row[3]
			item['station_name'] = row[4]
			item['station_no'] = row[5]
			print(item)
			listtable.append(item)
		table = {}
		table['data'] = listtable
		return table
