
import sqlite3

articles = [
    { "title": "My article", "content": "blah blah blah", "author": 1, "date": "2017-07-16" },
    { "title": "My article 1", "content": "blah blah blah", "author": 2, "date": "2017-07-16"},
    { "title": "My article 2", "content": "blah blah blah", "author": 2, "date": "2017-07-16"},
    { "title": "My article 3", "content": "blah blah blah", "author": 2, "date": "2017-07-16"},
    { "title": "My article 4", "content": "blah blah blah", "author": 2, "date": "2017-07-16"},
]

authors = [
    { "id": 1, "name": "Nicholas"},
    { "id": 2, "name": "Jonathan"}
]

conn = sqlite3.connect('spec.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS articles");

c.execute("DROP TABLE IF EXISTS authors");

conn.commit()

CREATE_ARTICLES_TABLE_STATEMENT = "CREATE TABLE IF NOT EXISTS articles ('title' string, 'content' string, 'author_id' integer, 'date' date);"

CREATE_AUTHORS_TABLE_STATEMENT = "CREATE TABLE IF NOT EXISTS  authors ('id' integer, 'name' string);"

c.execute(CREATE_ARTICLES_TABLE_STATEMENT);
c.execute(CREATE_AUTHORS_TABLE_STATEMENT);

conn.commit()

ARTICLES_SQL_STATEMENT = "INSERT INTO articles (title, content, author_id, date) VALUES ('%s', '%s', '%s', '%s');"

for article in articles:
    c.execute(ARTICLES_SQL_STATEMENT % (article["title"], article["content"], article["author"], article["date"]))

AUTHORS_SQL_STATEMENT = "INSERT INTO authors (id, name) VALUES ('%s', '%s');"

for author in authors:
    c.execute(AUTHORS_SQL_STATEMENT % (author["id"], author["name"]))

conn.commit()
conn.close()
