__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from datetime import datetime
from lib import db, security
from sqlalchemy import event

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.Boolean)
    email = db.Column(db.String(200))
    password = db.Column(db.String)
    salt = db.Column(db.String(200))
    registered_at = db.Column(db.DateTime)

@event.listens_for(Account, 'before_insert')
def before_insert(mapper, connection, instance):
    instance.registered_at = datetime.utcnow()
    instance.salt = security.generate_salt()
    instance.password = security.hash_password(instance.salt, instance.password)
