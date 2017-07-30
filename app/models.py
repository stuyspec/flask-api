from app import db


class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    slug = db.Column(db.String(500))
    content = db.Column(db.Text)
    date_time = db.Column(db.DateTime)
    volume = db.Column(db.Integer)
    issue = db.Column(db.Integer)
    is_draft = db.Column(db.Boolean)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    slug = db.Column(db.String(500))
    description = db.Column(db.Text)
    parent_slug = db.Column(db.String(500))

    article_id = db.relationship('Article', backref='section', lazy='dynamic')


class Issuu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    volume = db.Column(db.Integer)
    issue = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))
    description = db.Column(db.Text)
