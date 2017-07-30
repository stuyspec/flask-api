from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
article = Table('articles', post_meta,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('title', String(length=500)),
                Column('titleSlug', String(length=500)),
                Column('content', Text),
                Column('p_index', Integer),
                Column('timestamp', DateTime),
                Column('volume', Integer),
                Column('issue', Integer),
                Column('section_id', Integer),
                Column('subsection_id', Integer),
                )

article_tag = Table('article_tags', post_meta,
                    Column('id', Integer, primary_key=True, nullable=False),
                    Column('article_id', Integer),
                    Column('tag_id', Integer),
                    )

media = Table('media', post_meta,
              Column('id', Integer, primary_key=True, nullable=False),
              Column('user_id', Integer),
              Column('article_id', Integer),
              Column('url', String(length=600)),
              Column('title', String(length=500)),
              Column('caption', String(length=500)),
              Column('isFeatured', Boolean),
              Column('isPhoto', Boolean),
              )

role = Table('roles', post_meta,
             Column('id', Integer, primary_key=True, nullable=False),
             Column('title', String(length=200)),
             )

role_user = Table('user_roles', post_meta,
                  Column('id', Integer, primary_key=True, nullable=False),
                  Column('user_id', Integer),
                  Column('role_id', Integer),
                  )

section = Table('sections', post_meta,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('name', String(length=500)),
                Column('description', Text),
                )

user_article = Table('authorships', post_meta,
                     Column('id', Integer, primary_key=True, nullable=False),
                     Column('user_id', Integer),
                     Column('article_id', Integer),
                     )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].create()
    post_meta.tables['article_tag'].create()
    post_meta.tables['media'].create()
    post_meta.tables['role'].create()
    post_meta.tables['role_user'].create()
    post_meta.tables['section'].create()
    post_meta.tables['user_article'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].drop()
    post_meta.tables['article_tag'].drop()
    post_meta.tables['media'].drop()
    post_meta.tables['role'].drop()
    post_meta.tables['role_user'].drop()
    post_meta.tables['section'].drop()
    post_meta.tables['user_article'].drop()
