from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False)),
    Column('email', String(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False)),
    Column('role', SmallInteger),
)

user = Table('user', post_meta,
    Column('username', String(length=64, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
    Column('email', String(length=120, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['user'].drop()
