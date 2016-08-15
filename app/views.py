from flask import render_template, flash, redirect, url_for
from app import app
from .forms import CreateArticleForm

@app.route('/')
@app.route('/index')
def index():
	entries = [
		{
			'title': 'Hello',
			'content': 'Lorem ipsum..'
		}
	]
	return render_template('index.html', entries=entries)

@app.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateArticleForm()
	if form.validate_on_submit():
		print('%s %s' % (form.title.data, form.content.data))
		return redirect(url_for('index'))
		
	return render_template('create.html', form=form)