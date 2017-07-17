from app import db, Section, Article

db.drop_all()
db.create_all()

news = Section(name="News", slug="news", description="The news.")
opinions = Section(name="Opinions", slug="opinions", description="The opinions.")

jerryNews = Article(title="Jerry News", slug="jerry-news", section=news)
jasonOp = Article(title="Jason Opinions", slug="jason-opinions", section=opinions)

print news.articles.all()
print opinions.articles.all()
print jerryNews.section
