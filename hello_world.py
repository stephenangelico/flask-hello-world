from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
	return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
	html = """
		<h1>
			Hello {}!
		</h1>
		<p>
			If you are reading this, the web server was set up correctly. (TM)
		</p>
		<img src "http://http.cat/200">
	"""
	return html.format(name.title())

if __name__ == "__main__":
	app.run(host=environ['IP'],
		port=int(environ['PORT']))
