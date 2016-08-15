from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class CreateArticleForm(Form):
	title = StringField('title', validators=[DataRequired()])
	content = TextAreaField('content', validators=[DataRequired()])