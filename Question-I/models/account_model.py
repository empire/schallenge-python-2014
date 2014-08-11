__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import sqlalchemy as sa
from datetime import datetime
from lib import db, security
from sqlalchemy import event

from sqlalchemy_utils import EmailType

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column('id', db.Integer, primary_key=True)
    username = sa.Column(sa.Unicode(100), nullable = False, unique = True)
    email = sa.Column(EmailType, nullable = False, unique = True)
    password = db.Column(db.String, nullable=False)

    salt = db.Column(db.String(200))
    registered_at = db.Column(db.DateTime)

@event.listens_for(Account, 'before_insert')
def before_insert(mapper, connection, instance):
    instance.registered_at = datetime.utcnow()
    instance.salt = security.generate_salt()
    instance.password = security.hash_password(instance.salt, instance.password)
