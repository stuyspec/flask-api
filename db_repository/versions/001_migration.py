from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
user = Table('users', post_meta,
             Column('id', Integer, primary_key=True, nullable=False),
             Column('fname', String(length=128)),
             Column('lname', String(length=128)),
             Column('nickname', String(length=128)),
             Column('username', String(length=128)),
             Column('password', String(length=1024)),
             Column('email', String(length=1024)),
             Column('permissions', String(length=1024)),
             )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['email'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['email'].drop()
