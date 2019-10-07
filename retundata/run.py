from flask import Flask,request
from login_reg import Login_Reg
app = Flask(__name__)
@app.route('/')
def rootpage():
	return "hello world"

@app.route('/api/login',methods=['post','get'])
def login():
	user = request.args.get('name')
	passw = request.args.get('passw')
	x = Login_Reg()
	result = x.check(user,passw)
	return result

if __name__=='__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)