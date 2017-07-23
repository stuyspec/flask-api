import sqlite3
conn = sqlite3.connect("spec.db")
c = conn.cursor()

CREATE_ARTICLES = '''CREATE TABLE IF NOT EXISTS articles 
('id' integer, 'title' String, 'content' text, 'author' integer, 'date' date, 
'sectionID' integer)'''
CREATE_SECTIONS = "CREATE TABLE IF NOT EXISTS sections ('id' integer, 'title' String)"
CREATE_AUTHORS = "CREATE TABLE IF NOT EXISTS authors ('id' integer, 'name' String)"

ARTICLES_SQL_STATEMENT = '''INSERT INTO articles (id, title, content, author, date, sectionID) 
VALUES ('%d', '%s','%s', '%d', '%s', '%d');'''
SECTIONS_SQL_STATEMENT = "INSERT INTO sections (id, title) VALUES ('%d','%s');"
AUTHORS_SQL_STATEMENT = "INSERT INTO authors (id, name) VALUES ('%d','%s');"

articles = [
    (1, "Some article title 1", "Lorem ipsum consector dolor", 1, "2017-12-05", 1),
    (2, "Some article title 2", "Lorem ipsum consector dolor", 2, "2017-07-06", 3),
    (3, "Some article title 3", "Lorem ipsum consector dolor", 1, "2017-07-06", 2)
]

authors = [
    (1, "Jonathan"),
    (2, "Nicholas")
]

sections = [
    (1, "Arts and Entertainment"),
    (2, "Humor"),
    (3, "Opinions")
]

c.execute(CREATE_ARTICLES)
c.execute(CREATE_SECTIONS)
c.execute(CREATE_AUTHORS)

for article in articles:
    c.execute(ARTICLES_SQL_STATEMENT % article)

for section in sections:
    c.execute(SECTIONS_SQL_STATEMENT % section)

for author in authors:
    c.execute(AUTHORS_SQL_STATEMENT % author)    

conn.commit()
conn.close()

