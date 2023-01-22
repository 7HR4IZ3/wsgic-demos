from flask import Flask

app = Flask (__name__)
app.debug = True

@app.route("/")
def hello_world ():
	return 'Hello World! from flask'

@app.route("/test")
def test():
	return "Test"
