from app import db

class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), index=True, unique=False)
	content = db.Column(db.String(500), index=True, unique=False)

	def __repr__(self):
		return title