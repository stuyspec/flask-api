#!flask/bin/python
from app import models, db
from datetime import datetime


section_sample  =  models.Section(name = "humor",
                                  slug = "humorstuff",
                                  description = "this is the humor department")

subsection_sample  =  models.Subsection(name = "year_review",
                                        slug = "more_humor_stuff",
                                        description = "this is humor department",
                                        parent = "humor" )

article_sample  =  models.Article(
    title = "george thingy",
    slug = "george_thingy",
    content = "good riddance and thank god",
    date_time = datetime.today(),
    volume = 111,
    issue = 12,
    is_draft = False,
    section = section_sample,
    subsection = subsection_sample
)


more_sample = models.Article(
    title = "jason thingy",
    slug = "jason_thingy",
    content = "gasdsaood riddance and thank god",
    date_time = datetime.today(),
    volume = 111,
    issue = 12,
    is_draft = False,
    section = section_sample,
    subsection = subsection_sample
)

db.session.add(section_sample)
db.session.add(subsection_sample)
db.session.add(article_sample)
db.session.add(more_sample)
db.session.commit()


article_sample = models.Article(
    title = "geoasdsadrge potato",
    slug = "geoasfe_thingy",
    content = "good fsafagod",
    date_time = datetime.today(),
    volume = 5,
    issue = 112,
    is_draft = False,
    section = section_sample,
    subsection = subsection_sample
)

more_sample = models.Article(
    title = "jasonasnj thingy",
    slug = "jasond_thingy",
    content = "gsfaafagod",
    date_time = datetime.today(),
    volume = 5,
    issue = 112,
    is_draft = True,
    section = section_sample,
    subsection = subsection_sample
)

db.session.add(article_sample)
db.session.add(more_sample)

db.session.commit()

issuu_one = models.Issuu(code = "111/12",
                         volume = 111,
                         issue = 12)

issuu_two = models.Issuu(code = "5/112",
                         volume = 5,
                         issue = 112)

db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()


issuu_one = models.User(
    first_name = "jason",
    last_name = "kao",
    username = "jkao",
    password = "donut",
    email = "jkao@stuy.edu",
    description = "avocado"
)


issuu_two = models.User(
    first_name = "geprge",
    last_name = "zheng",
    username = "gz",
    password = "asad",
    email = "gzhen@stuy.edu",
    description = "peanut"
)


db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()


print "done"
