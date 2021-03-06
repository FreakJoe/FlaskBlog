from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='{#',
        comment_end_string='#}',
    ))

app = CustomFlask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models