from app import db
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(200))
    name = db.Column(db.String(200))
    importance = db.Column(db.Integer)

class Issuu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))

    role = db.relationship('RoleUser', backref='uzer', lazy='dynamic')
    articles = db.relationship('UserArticle', backref='uzer', lazy='dynamic')
    media = db.relationship('Media', backref='uzer', lazy='dynamic')

RoleUser = db.Table('RoleUsers',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))

UserArticle = db.Table('UserArticles',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    titleSlug = db.Column(db.String(500))
    content = db.Column(db.Text)
    p_index = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    volume = db.Column(db.Integer)
    issue = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    subsection_id = db.Column(db.Integer)

    posts = db.relationship('UserArticle', backref='author', lazy='dynamic')
    medias = db.relationship('Media', backref='author', lazy='dynamic')
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    subsection_id = db.Column(db.Integer, db.ForeignKey('subsection.id'))

class Media(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)
    url = db.Column(db.String(600))
    title = db.Column(db.String(500))
    caption = db.Column(db.String(500))
    isFeatured = db.Column(db.Boolean)
    isPhoto = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))



ArticleTag = db.Table('ArticleTags',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Section(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))
    description = db.Column(db.Text)
    foo = db.relationship('Article', backref='author', lazy='dynamic')

class Subsection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))
    description = db.Column(db.Text)    

    foo = db.relationship('Article', backref='author', lazy='dynamic')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))

    foo = db.relationship('ArticleTag', backref='author', lazy='dynamic')