__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from register import *
from login_route import *
from activation_route import *
from migration_route import *

from lib import app
from flask import request, flash, url_for, redirect, \
     render_template

from models import Account

@app.route('/')
def home():
    return render_template('show_all.html',
        todos=Account.query.order_by(Account.registered_at.desc()).all()
    )
