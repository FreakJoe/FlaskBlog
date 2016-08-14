from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", entries=[
			{
				'title': 'Hello',
				'content': 'Lorem ipsum..'
			}
		])

@app.route('/create')
def create():
	return render_template("create.html")