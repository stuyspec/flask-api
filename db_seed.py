from datetime import datetime

from app import models, db

seed_data = {
    "sections" : [
        {
            "name": "Humor",
            "slug": "humor",
            "description": "Jason Kao's face",
            "parent_slug": None
        },
        {
            "name": "News",
            "slug": "news",
            "description": "All News That's Fit to Skim As You Walk On The Bridge",
            "parent_slug": None
        },
        {
            "name": "Arts & Entertainment",
            "slug": "arts-entertainment",
            "description": "Paintings of Horses And Ships"
        }
    ],
    "articles": [
        {
            "title": "J'accuse",
            "slug": "jaccuse",
            "content": "Would you allow me, grateful as I am for the kind reception" \
            " you once extended to me, to show my concern about maintaining your "\
            "well-deserved prestige and to point out that your star which, until now," \
            "has shone so brightly, risks being dimmed by the most shameful and indelible"\
            " of stains? ",
            "volume": 111,
            "issue": 12,
            "is_draft": False,
            "section": 1
        },
        {
            "title": "Kennedy Is Killed By Spiner",
            "slug": "kennedy-is-killed-by-cia",
            "content": "Dallas, Nov. 22--President John Fitzgerald Kennedy was"\
            "shot and killed by an assassin today. He died of a wound in the "\
            "brain caused by a rifle bullet that was fired at him as he was "\
            "riding through downtown Dallas in a motorcade. Vice President "\
            "Lyndon Baines Johnson, who was riding in the third car behind "\
            "Mr. Kennedy's, was sworn in as the 36th President of the United "\
            "States 99 minutes after Mr. Kennedy's death.",
            "volume": 111,
            "issue": 13,
            "is_draft": False,
            "section": 0
        }
    ],
    "users": [
        {
            "first_name": "Nicholas",
            "last_name": "Yang",
            "username": "nicholaslyang",
            "password": "hunter2",
            "email": "nicholasleeyang@gmail.com",
            "description": "Best programmer ever"
        },
        {
            "first_name": "Jason",
            "last_name": "Kao",
            "username": "jkao1",
            "password": "washmyface",
            "email": "jkao1@stuy.edu",
            "description": "Most mediocre programmer ever"
        }
    ]
}

section_sample = models.Section(name="humor",
                                slug="humorstuff",
                                description="this is the humor department")

article_sample = models.Article(
    title="george thingy",
    slug="george_thingy",
    content="good riddance and thank god",
    date_time=datetime.today(),
    volume=111,
    issue=12,
    is_draft=False,
    section=section_sample,
)

more_sample = models.Article(
    title="jason thingy",
    slug="jason_thingy",
    content="gasdsaood riddance and thank god",
    date_time=datetime.today(),
    volume=111,
    issue=12,
    is_draft=False,
    section=section_sample,
)

db.session.add(section_sample)
db.session.add(article_sample)
db.session.add(more_sample)
db.session.commit()

article_sample = models.Article(
    title="geoasdsadrge potato",
    slug="geoasfe_thingy",
    content="good fsafagod",
    date_time=datetime.today(),
    volume=5,
    issue=112,
    is_draft=False,
    section=section_sample,
)

more_sample = models.Article(
    title="jasonasnj thingy",
    slug="jasond_thingy",
    content="gsfaafagod",
    date_time=datetime.today(),
    volume=5,
    issue=112,
    is_draft=True,
    section=section_sample,
)

db.session.add(article_sample)
db.session.add(more_sample)

db.session.commit()

issuu_one = models.Issuu(code="111/12",
                         volume=111,
                         issue=12)

issuu_two = models.Issuu(code="5/112",
                         volume=5,
                         issue=112)

db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()

issuu_one = models.User(
    first_name="jason",
    last_name="kao",
    username="jkao",
    password="donut",
    email="jkao@stuy.edu",
    description="avocado"
)

issuu_two = models.User(
    first_name="geprge",
    last_name="zheng",
    username="gz",
    password="asad",
    email="gzhen@stuy.edu",
    description="peanut"
)

db.session.add(issuu_one)
db.session.add(issuu_two)
db.session.commit()
