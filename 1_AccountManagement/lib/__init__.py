__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from user_activation import *
from config import config_db

app = Flask(__name__, template_folder='../templates')
app.config.from_pyfile('../config/app.cfg')

config_db(app)

handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
