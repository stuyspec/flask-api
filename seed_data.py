from app import db, Section, Article
import datetime

db.drop_all()
db.create_all()

# create sections
news = Section(name="News", slug="news", description="The news.")
opinions = Section(name="Opinions", slug="opinions", description="The opinions.")
features = Section(name="Features", slug="features", description="The features.")
ae = Section(name="Arts & Entertainment", slug="ae", description="The arts & entertainment.")
humor = Section(name="Humor", slug="humor", description="The humor.")
sports = Section(name="Sports", slug="sports", description="The sports.")
art = Section(name="Art", slug="art", description="The art.")
photo = Section(name="Photo", slug="photo", description="The photo.")
video = Section(name="Video", slug="video", description="The video.")

# link subsections
Section(name="2014 Campaign Coverage", slug="2014-campaign-coverage", description="The 2014 campaign coverage.", parent=news)
Section(name="2016 Campaign Coverage", slug="2016-campaign-coverage", description="The 2016 campaign coverage.", parent=news)
Section(name="2017 Campaign Coverage", slug="2017-campaign-coverage", description="The 2017 campaign coverage.", parent=news)
Section(name="Staff Editorials", slug="staff-editorials", description="The staff editorials.", parent=opinions)
Section(name="9/11", slug="9-11", description="The 9/11.", parent=features)
Section(name="College Essays", slug="college-essays", description="The college essays.", parent=features)
Section(name="VOICES", slug="voices", description="The voices.", parent=features)
Section(name="Art", slug="art", description="The art.", parent=ae)
Section(name="Books", slug="books", description="The books.", parent=ae)
Section(name="Feature", slug="feature", description="The feature.", parent=ae)
Section(name="Film", slug="film", description="The film.", parent=ae)
Section(name="Food", slug="food", description="The food.", parent=ae)
livePerformances = Section(name="Live Performances", slug="live-performances", description="The live performances.", parent=ae)
Section(name="Music", slug="music", description="The music.", parent=ae)
Section(name="Television", slug="television", description="The television.", parent=ae)
Section(name="Film", slug="film", description="The film.", parent=ae)
Section(name="Disrespectator", slug="disrespectator", description="The disrespectator.", parent=humor)
Section(name="Spooktator", slug="spooktator", description="The spooktator.", parent=humor)

# link subsubsections
Section(name="SING!", slug="sing", description="The SING!.", parent=livePerformances)
Section(name="Stuyvesant Theater Community", slug="stc", description="The STC.", parent=livePerformances)

# create example articles
Article(title="Apples Rain in New York City",
        slug="apples-rain-in-new-york-city",
        content="Apples rain. Oranges do not.",
        datetime=datetime.datetime.utcnow(),
        volume=108,
        issue=2,
        isDraft=False,
        section=news)
Article(title="Bananas Fall in Boston: Opinion Piece",
        slug="bananas-fall-in-boston",
        content="Bananas fall. Kiwis do not.",
        datetime=datetime.datetime.utcnow(),
        volume=108,
        issue=2,
        isDraft=False,
        section=opinions)

db.session.add(news)
db.session.add(opinions)
db.session.add(features)
db.session.add(ae)
db.session.add(humor)
db.session.add(sports)
db.session.add(art)
db.session.add(photo)
db.session.add(video)
db.session.add(livePerformances)

db.session.commit()
