from flask import render_template, flash, redirect, url_for
from app import app, db, models
from .forms import CreateArticleForm

@app.route('/')
@app.route('/index')
def index():
	entries = models.Article.query.all()
	return render_template('index.html', entries=entries)

@app.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateArticleForm()
	if form.validate_on_submit():
		a = models.Article(title=form.title.data, content=form.content.data)
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('index'))
		
	return render_template('create.html', form=form)