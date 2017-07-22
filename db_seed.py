#!flask/bin/python
from app import models, db
from datetime import datetime


section_sample = models.Section(name="humor",slug="humorstuff",description="this is the humor department")

subsection_sample = models.Subsection(name="year_review",slug="more_humor_stuff",description="this is humor department")

article_sample = models.Article(title="george thingy",slug="george_thingy",content="good riddance and thank god",
     datetime=datetime.today(),volume=111,issue=12,isDraft=False,section=section_sample,subsection=subsection_sample)


more_sample = models.Article(title="jason thingy",slug="jason_thingy",content="gasdsaood riddance and thank god",
     datetime=datetime.today(),volume=111,issue=12,isDraft=False,section=section_sample,subsection=subsection_sample)

db.session.add(section_sample)
db.session.add(subsection_sample)
db.session.add(article_sample)
db.session.add(more_sample)
db.session.commit()


article_sample = models.Article(title="geoasdsadrge potato",slug="geoasfe_thingy",content="good fsafagod",
     datetime=datetime.today(),volume=5,issue=112,isDraft=False,section=section_sample,subsection=subsection_sample)

more_sample = models.Article(title="jasonasnj thingy",slug="jasond_thingy",content="gsfaafagod",
     datetime=datetime.today(),volume=5,issue=112,isDraft=True,section=section_sample,subsection=subsection_sample)

db.session.add(article_sample)
db.session.add(more_sample)

db.session.commit()

issuu_one = models.Issuu(code="111/12", volume=111, issue=12)

issuu_two = models.Issuu(code="5/112", volume=5, issue=112)

db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()


issuu_one = models.User(firstname="jason", lastname="kao", username="jkao",password="donut",email="jkao@stuy.edu",description="avocado")


issuu_two = models.User(firstname="geprge", lastname="zheng", username="gz",password="asad",email="gzhen@stuy.edu",description="peanut")


db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()


print "done"
