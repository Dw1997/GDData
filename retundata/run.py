from flask import Flask,request,jsonify,render_template
from login_reg import Login_Reg
from getlinere import getinform
from yuanzun import getxs
from return_news import Renews

app = Flask(__name__)
@app.route('/')
def rootpage():
	return render_template('index.html')

@app.route('/yz')
def yzapi():
    x = getxs()
    y = x.GETZY()
    z = x.GETBW(y)
    return z[1]

@app.route('/api/train',methods=['post','get'])
def trainapi():
	print(type(request.args.get('name')))
	abs = request.args.get('name')
	item = getinform()
	some = item.gettimetable(abs)
	return jsonify(some)

@app.route('/api/login',methods=['post','get'])
def login():
	user = request.args.get('name')
	passw = request.args.get('passw')
	x = Login_Reg()
	result = x.check(user,passw)
	if result:
		return jsonify({'result':'success'})
	else:
		return jsonify({'result':'fail'})

@app.route('/api/register',methods=['post','get'])
def register():
	userphone = request.args.get('userphone')
	username = request.args.get('username')
	usermail = request.args.get('usermail')
	userpass = request.args.get('userpass')
	x = Login_Reg()
	result = x.register(userphone,username,usermail,userpass)
	re = {}
	if result==True:
		re['data'] = 'success'
	else:
		re['data'] = 'fail'
	return jsonify(re)

@app.route('/api/news',methods=['post','get'])
def renews():
	num = request.args.get('num')
	i = int(num)
	x = Renews()
	data = x.fkrenews(i)
	return jsonify(data)

if __name__=='__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)