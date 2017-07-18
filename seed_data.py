from app import db, Section, Article
import datetime

db.drop_all()
db.create_all()

news = Section(name="News", slug="news", description="The news.")
opinions = Section(name="Opinions", slug="opinions", description="The opinions.")

apple = Article(title="Apples Rain in New York City",
                slug="apples-rain-in-new-york-city",
                content="Apples rain. Oranges do not.",
                datetime=datetime.datetime.utcnow(),
                volume=108,
                issue=2,
                isDraft=False,
                section=news)

banana = Article(title="Bananas Fall in Boston: Opinion Piece",
                 slug="bananas-fall-in-boston",
                 content="Bananas fall. Kiwis do not.",
                 datetime=datetime.datetime.utcnow(),
                 volume=108,
                 issue=2,
                 isDraft=False,
                 section=opinions)

db.session.add(news)
db.session.add(opinions)
db.session.add(apple)
db.session.add(banana)
db.session.commit()
