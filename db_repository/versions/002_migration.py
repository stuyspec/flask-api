from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('fname', VARCHAR(length=128)),
    Column('lname', VARCHAR(length=128)),
    Column('nickname', VARCHAR(length=128)),
    Column('username', VARCHAR(length=128)),
    Column('password', VARCHAR(length=1024)),
    Column('email', VARCHAR(length=1024)),
    Column('permissions', VARCHAR(length=1024)),
)

advertisement = Table('advertisement', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=200), primary_key=True, nullable=False),
    Column('name', String(length=200), primary_key=True, nullable=False),
    Column('importance', Integer, primary_key=True, nullable=False),
)

issuu = Table('issuu', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('code', Integer, primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['advertisement'].create()
    post_meta.tables['issuu'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['advertisement'].drop()
    post_meta.tables['issuu'].drop()
