import Flask
app = Flask(__name__)
@app.route('/')
def rootpage():
	return "hello world"

if __name__=='__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)