from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
project = Table('project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
    Column('owner', String(length=64, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False)),
    Column('description', Text(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False)),
    Column('created', DateTime(timezone=False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['project'].columns['id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['project'].columns['id'].drop()
