from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os
import calendar

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(tempfile.gettempdir(), "test.db")#For windows only, will change back in a few days - Jerry 
db = SQLAlchemy(app)

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    description = db.Column(db.Text)
    articles = db.relationship('Article', backref='section', lazy='dynamic')
    parent_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    subsections = db.relationship(
        'Section',
        backref=db.backref('parent', remote_side=[id])
    )

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

def find_section(section_slug, subsection_slug):
    targetedSection = Section.query.filter(Section.slug == section_slug).first()
    if subsection_slug != 'main':
        for subsection in targetedSection.subsections:
            if subsection.slug == subsection_slug:
                return targetedSection
    else:
        return targetedSection
def create_date(date):#Takes a dateTime object and modifies it into a specially formatted string for the date
    month_number = date.month
    month_name = calendar.month_name[month_number]
    return month_name + " " + str(date.day) + ", " + str(date.year)
def create_time(time):#Takes a dateTime object and modifies it into a specially formatted string for the time
    hour = time.hour
    if hour > 12:
        hour -= 12
    minute = time.minute
    if minute == 0:
        minute = "00"
    if time.hour >= 12:
        return str(hour) + ":" + str(minute) + " PM"
    else:
        return str(hour) + ":" + str(minute) + " AM"

@app.route('/sections/<string:section_slug>/subsections/<string:subsection_slug>', methods=['GET'])
def show_section(section_slug, subsection_slug):
    targetedSection = find_section(section_slug, subsection_slug)
    if targetedSection == None:
        return "Please input a proper section slug!"
    return jsonify(
        {
            "name": targetedSection.name,
            "description": targetedSection.description,
            "slug": targetedSection.slug,
        }
    )

@app.route('/sections/<string:section_slug>/subsections/<string:subsection_slug>/articles', methods=['GET'])
def show_section_articles(section_slug, subsection_slug):
    targetedSection = find_section(section_slug, subsection_slug)
    if targetedSection == None:
        return "Please input a proper section slug!"
    nonSerializableArticles = targetedSection.articles.all()
    serializableArticles = []
    for article in nonSerializableArticles:
        serializableArticle = {
            "title": article.title,
            "content": article.content,
            "volume": article.volume,
            "issue": article.issue
            }
        serializableArticles.append( serializableArticle )
    return jsonify(
        {
            "name": targetedSection.name,
            "description": targetedSection.description,
            "slug": targetedSection.slug,
            "articles": serializableArticles
        }
    )

@app.route('/sections/<string:section_slug>/subsections/<string:subsection_slug>/articles/<string:article_slug>', methods=['GET'])
def show_article(section_slug, article_slug, subsection_slug):
    targetedSection = find_section(section_slug, subsection_slug)
    allArticles = targetedSection.articles.all()
    for article in allArticles:
        if article.slug == article_slug:
            return jsonify(
            {
                "id": article.id,
                "title": article.title,
                "slug": article_slug,
                "content": article.content,
                "volume": article.volume,
                "issue": article.issue,
                "date": create_date(article.datetime),
                "time": create_time(article.datetime),
                "section": article.section_id
            }
        )
    return "Please input a proper article slug"
