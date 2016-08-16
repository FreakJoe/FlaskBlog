from flask_wtf import Form
from wtforms import StringField, TextAreaField, Label
from wtforms.validators import DataRequired

class CreateArticleForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])