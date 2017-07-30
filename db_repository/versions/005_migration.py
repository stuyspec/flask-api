from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
subsection = Table('subsection', post_meta,
                   Column('id', Integer, primary_key=True, nullable=False),
                   Column('name', String(length=500)),
                   Column('description', Text),
                   )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subsection'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subsection'].drop()
