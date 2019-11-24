from flask import Flask,request,jsonify,render_template
from login_reg import Login_Reg
from getlinere import getinform
from yuanzun import getxs
from return_news import Renews
from zhy_login_reg import ZHY_Login_Reg

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
		return jsonify({'result':result})
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

@app.route('/api/changep',methods=['post','get'])
def changep():
	phone = request.args.get('phone')
	oldp = request.args.get('oldp')
	newp = request.args.get('newp')
	x = Login_Reg()
	result = x.changep(phone,oldp,newp)
	return jsonify({'result':result})

@app.route('/api/news',methods=['post','get'])
def renews():
	num = request.args.get('num')
	i = int(num)
	x = Renews()
	data = x.fkrenews(i)
	return jsonify({'result':data})

@app.route('/api/addlog',methods=['post','get'])
def addlogs():
	user = request.args.get('user')
	newsid = request.args.get('id')
	x = Renews()
	result = x.addlog(newsid,user)
	return jsonify({'result':result})

@app.route('/zhy/api/login',methods = ['post','get'])
def zhylogin():
	user = request.args.get('name')
	passw = request.args.get('passw')
	x = ZHY_Login_Reg()
	result = x.check(user,passw)
	if result:
		return jsonify({'result':result})
	else:
		return jsonify({'result':'fail'})

@app.route('/zhy/api/reg',methods=['post','get'])
def zhyreg():
	userphone = request.args.get('phone')
	username = request.args.get('name')
	userpass = request.args.get('pass')
	useraddr = request.args.get('addr')
	areaid = request.args.get('area')
	x = ZHY_Login_Reg()
	result = x.register(userphone,username,userpass,useraddr,areaid)
	if result:
		return jsonify({'result': result})
	else:
		return jsonify({'result': result})

@app.route('/zhy/api/addposter',methods=['post','get'])
def zhyaddposter():
	userphone = request.args.get('phone')
	username = request.args.get('name')
	userpass = request.args.get('pass')
	areaid = request.args.get('area')
	x = ZHY_Login_Reg()
	result = x.addposter(userphone,username,userpass,areaid)
	if result:
		return jsonify({'result': result})
	else:
		return jsonify({'result': result})


@app.route('/zhy/api/changepass',methods=['post','get'])
def zhychagnge():
	userphone = request.args.get('phone')
	userpass = request.args.get('oldp')
	newpass = request.args.get('newp')
	x = ZHY_Login_Reg()
	result = x.changepass(userphone,userpass,newpass)
	return jsonify({'result':result})


@app.route('/zhy/api/orders',methods=['post','get'])
def zhyorders():
	whoo = request.args.get('who')
	userphone = request.args.get('phone')
	gp = request.args.get('gp')
	x = ZHY_Login_Reg()
	result = x.orders(whoo,userphone,gp)
	return jsonify({'result':result})



if __name__=='__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)