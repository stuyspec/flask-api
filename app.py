from flask import Flask, jsonify
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
                targetedSection = subsection
    return targetedSection

@app.route('/sections/<string:section_slug>/subsections/<string:subsection_slug>', methods=['GET'])
def show_section(section_slug, subsection_slug):
    targetedSection = find_section(section_slug, subsection_slug)
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

@app.route('/sections/<string:section_slug>/articles/<string:article_slug>', methods=['GET'])
def show_article(section_slug, article_slug):
    targetedSection = find_section(section_slug, subsection_slug)
    allArticles = targetedSection.articles.all()
    for article in allArticles:
        if article.slug == article_slug:
            return jsonify(
            {
                "title": article.title,
                "content": article.content,
                "volume": article.volume,
                "issue": article.issue
            }
        )
