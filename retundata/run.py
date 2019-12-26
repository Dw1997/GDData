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


@app.route('/api/news',methods = ['get','post'])
def renews():
	typee = request.args.get('tp')
	num = request.args.get('page')
	x = Renews()
	data = x.re_news_n(typee,num)
	return jsonify({'result':data})

# 返回新闻类别
@app.route('/api/newstp',methods = ['get','post'])
def renewstp():
	x = Renews()
	data = x.re_news_tp()
	return jsonify({'result':data})

# @app.route('/api/news',methods=['post','get'])
# def renews():
# 	num = request.args.get('num')
# 	i = int(num)
# 	x = Renews()
# 	data = x.fkrenews(i)
# 	return jsonify({'result':data})

@app.route('/api/addlog',methods=['post','get'])
def addlogs():
	user = request.args.get('user')
	newsid = request.args.get('id')
	x = Renews()
	result = x.addlog(newsid,user)
	return jsonify({'result':result})

@app.route('/api/addlog2',methods=['post','get'])
def addlogs2():
	newid = request.args.get('nid')
	pid = request.args.get('pid')
	ty = request.args.get('tp')
	x = Renews()
	result = x.addlog2(newid,pid,ty)
	return jsonify({'result':result})


@app.route('/api/delcon',methods=['post','get'])
def delcolnew():
	newdi = request.args.get('id')
	pg = request.args.get('ph')
	x = Renews()
	result = x.delcon(newdi,pg)
	return jsonify({'result': result})


@app.route('/api/coat',methods=['post','get'])
def rcoat():
	tp = request.args.get('tp')
	x = Renews()
	result = x.rcogo(tp)
	return jsonify({'result':result})

@app.route('/api/uco',methods=['get','post'])
def ruco():
	ph = request.args.get('ph')
	x = Renews()
	result = x.ruco(ph)
	return jsonify({'result': result})

@app.route('/api/deln',methods=['get','post'])
def delnew():
	id = request.args.get('id')
	x = Renews()
	result = x.deln(id)
	return jsonify({'result': result})

@app.route('/api/top20',methods=['get','post'])
def top20n():
	x = Renews()
	result = x.top20()
	return jsonify({'result':result})

@app.route('/api/search',methods=['get','post'])
def searchnews():
	typee = request.args.get('tp')
	searcchitem = request.args.get('it')
	x = Renews()
	result = x.newsearch(typee,searcchitem)
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


# 获取小区内快递
@app.route('/zhy/api/orders',methods=['post','get'])
def zhyorders():
	whoo = request.args.get('who')
	userphone = request.args.get('phone')
	gp = request.args.get('gp')
	x = ZHY_Login_Reg()
	result = x.orders(whoo,userphone,gp)
	return jsonify({'result':result})

@app.route('/zhy/api/poster_send',methods=['post','get'])
def zhyposter_send():
	phone = request.args.get('ph')
	addr = request.args.get('ad')
	areaid = request.args.get('ai')
	x = ZHY_Login_Reg()
	result = x.poster_send(phone,addr,areaid)
	return jsonify({'result':result})

@app.route('/zhy/api/user_send',methods=['get','post'])
def zhyuser_send():
	uphone = request.args.get('up')
	gname = request.args.get('gn')
	gphone = request.args.get('gh')
	gaddr = request.args.get('ga')
	x = ZHY_Login_Reg()
	result = x.user_send(uphone,gname,gphone,gaddr)
	return jsonify({'result':result})

@app.route('/zhy/api/user_out',methods=['get','post'])
def zhyuser_out():
	phone = request.args.get('ph')
	x = ZHY_Login_Reg()
	result = x.return_out(phone)
	return jsonify({'result':result})

# 快递员根据小区id获取要发出快递	
@app.route('/zhy/api/gp',methods=['get','post'])
def zhyuser_out_all():
	areaid = request.args.get('ai')
	x = ZHY_Login_Reg()
	result = x.return_out_all(areaid)
	return jsonify({'result':result})

@app.route('/zhy/api/gper',methods=['get','post'])
def zhyget_per():
	typee = request.args.get('tp')
	aid = request.args.get('aid')
	x = ZHY_Login_Reg()
	result = x.return_per(typee,aid)
	return jsonify({'resule':result})

@app.route('/zhy/api/gan',methods=['get','post'])
def zhyget_an():
	typee = request.args.get('tp')
	uphone = request.args.get('up')
	x = ZHY_Login_Reg()
	result = x.return_inf_n_a(typee,uphone)
	return jsonify({'result':result})

@app.route('/zhy/api/getubp',methods=['get','post'])
def zhyget_user_b_p():
	uphone = request.args.get('up')
	x = ZHY_Login_Reg()
	result = x.return_user(uphone)
	return jsonify({'result':result})

# 快递员确认到家提取快递
@app.route('/zhy/api/getoit', methods=['get', 'post'])
def zhyget_out_it():
	itid = request.args.get('id')
	poser = request.args.get('ph')
	x = ZHY_Login_Reg()
	result = x.poser_get_it(itid,poser)
	return jsonify({'result':result})

# 用户给订单添加评论
@app.route('/zhy/api/uc', methods=['get', 'post'])
def zhy_uc():
	id = request.args.get('id')
	up = request.args.get('up')
	pp = request.args.get('pp')
	co = request.args.get('co')
	x = ZHY_Login_Reg()
	result = x.add_comment(id,up,pp,co)
	return jsonify({'result':result})

# 快递员确认园区内快递送达
@app.route('/zhy/api/sis',methods=['get','post'])
def zhy_sure_sended():
	id = request.args.get('id')
	x  = ZHY_Login_Reg()
	result = x.send_it(id)
	return jsonify({'result':result})

# 用户派送订单获取派送信息
@app.route('/zhy/api/ugp',methods=['get','post'])
def zhy_get_poser_inf():
	id = request.args.get('id')
	x = ZHY_Login_Reg()
	resurt = x.get_out_poser(id)
	return jsonify({'result':resurt})

# 快递员获取须发快递单子
@app.route('/zhy/api/nso',methods=['get','post'])
def zhy_get_n_out():
	id = request.args.get('id')
	x = ZHY_Login_Reg()
	resurt = x.get_out_orders(id)
	return jsonify({'result': resurt})

# 快递员给须发送快递添加运单号
@app.route('/zhy/api/ansi',methods=['get','post'])
def zhy_add_id_ns():
	id = request.args.get('id')
	kid = request.args.get('kid')
	x = ZHY_Login_Reg()
	result = x.ins_out_kdi(id,kid)
	return jsonify({'result':result})


@app.route('/zhy/api/repoc',methods=['get','post'])
def zhy_ret_poco():
	ph = request.args.get('ph')
	x = ZHY_Login_Reg()
	result = x.re_po_co(ph)
	return jsonify({'result':result})

@app.route('/zhy/api/deluser', methods=['get', 'post'])
def zhy_del_user():
	ph = request.args.get('ph')
	x = ZHY_Login_Reg()
	result = x.deluser(ph)
	return jsonify({'result': result})





if __name__=='__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)
