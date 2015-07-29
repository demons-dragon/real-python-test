from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello, World!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#integer path
@app.route("/integer/<int:value>")
def int_type(value):
	print value+1
	return "correct"

#float path
@app.route("/float/<float:value>")
def int_float(value):
	print value+1
	return "correct"

#string route
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "demons-dragon":
		return "Hello Mr. {}".format(name), 200
	else:
		return "Not found ", 404

if __name__ == "__main__":
	app.run()