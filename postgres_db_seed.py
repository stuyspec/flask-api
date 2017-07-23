import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from config import SQLALCHEMY_DATABASE_URI

def connect():
	con = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, client_encoding='utf8')
	meta = sqlalchemy.MetaData(bind=con, reflect=True)
	return con, meta

con, meta = connect()

if not con.dialect.has_table(con, "articles"):
	articles = Table('articles', meta,
		Column('name', String, primary_key=True),
		Column('author', String, ForeignKey('authors.name')),
		Column('content', String),
		Column('date', String)
	)

if not con.dialect.has_table(con, "authors"):
	authors = Table('authors', meta, 
		Column('name', String, primary_key=True),
		Column('bio', String))
meta.create_all(con)

def addAuthor(name, bio):
	statement = meta.tables["authors"].insert().values(name=name, bio=bio)
	con.execute(statement)

def addArticle(name, author, content, date):
	statement = meta.tables["articles"].insert().values(name=name, author=author, content=content, date=date)
	con.execute(statement)

addAuthor("Your True Friend", "I'm someone you can trust.")
addArticle("Tackling Unexpected Boundaries", "Your True Friend", "Sometimes it is best to leave things be. - A true friend", "DA FUTURE")