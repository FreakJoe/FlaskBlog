from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateArticleForm(Form):
	title = StringField('title', validators=[DataRequired()])
	content = StringField('content', validators=[DataRequired()])