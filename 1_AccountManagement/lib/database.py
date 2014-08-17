__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from alembic import command
from flask.ext.migrate import upgrade, history

from lib import db, app
from sqlalchemy.exc import OperationalError

def check_db():
    try:
        # Do migration, if there is migration version that is not applied, apply it
        upgrade()
        return True
    except OperationalError, e:
        app.logger.error("Somethings is happen wrong : " + e.message)
        pass

    return False
