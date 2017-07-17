from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    description = db.Column(db.Text)
    articles = db.relationship('Article', backref='section', lazy='dynamic')

    def __repr__(self):
        return '<Section %r>' % (self.name)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    content = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    volume = db.Column(db.Integer)
    issue = db.Column(db.Integer)
    isDraft = db.Column(db.Boolean)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))

    def __repr__(self):
        return '<Article %r>' % (self.title)


