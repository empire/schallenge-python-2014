__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import sqlalchemy as sa
from datetime import datetime, timedelta
from lib import app, db, security
from sqlalchemy import event
from sqlalchemy.orm import validates

from sqlalchemy_utils import EmailType

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column('id', db.Integer, primary_key=True)
    username = sa.Column(sa.Unicode(100), nullable=False, unique=True)
    email = sa.Column(EmailType, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    salt = db.Column(db.String(200))
    registered_at = db.Column(db.DateTime)
    #
    activation_code = db.Column(db.String, nullable=False)
    activation_code_generated_at = db.Column(db.DateTime, nullable=False)

    enabled = db.Column(db.Boolean, nullable=True)
    enabled_at = db.Column(db.DateTime, nullable=True)

    def __init__(self):
        pass

    def generate_activation_code(self):
        self.activation_code = security.generate_random_activation_code()
        self.activation_code_generated_at = datetime.utcnow()

    def is_activation_code_expired(self):
        current_time = datetime.utcnow()

        the_day_after = self.activation_code_generated_at + timedelta(days=1)
        app.logger.info(str(the_day_after) + " " + str(current_time) + " " + str(the_day_after <= current_time))

        return the_day_after <= current_time

    def activate(self):
        self.enabled_at = datetime.utcnow()
        self.enabled = True

def find_account_by_activation_code(code):
    return Account.query.filter(Account.activation_code == code).first()

def find_active_account_by_username_and_password(username, password):
    account = Account.query.filter(
        Account.username == username,
        Account.enabled == True
    ).first()
    if None == account:
        app.logger.info('No active account found' + username)
        return None
    app.logger.info('Active account ' + str(account))
    if security.check_password(account.password, account.salt, password):
        app.logger.info('Password is matched')
        return account
    app.logger.info('Password is not matched')
    return None

@event.listens_for(Account, 'before_insert')
def before_insert(mapper, connection, instance):
    instance.registered_at = datetime.utcnow()
    instance.salt = security.generate_salt()
    instance.password = security.hash_password(instance.salt, instance.password)
    instance.generate_activation_code()

@event.listens_for(Account, 'after_insert')
def send_verification_email(mapper, connection, instance):
    pass
