__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from register import *

from lib import app
from flask import request, flash, url_for, redirect, \
     render_template

from models import Account

@app.route('/')
def home():
    return render_template('show_all.html',
        todos=Account.query.order_by(Account.registered_at.desc()).all()
    )


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))

@app.route('/build-db', methods=['GET'])
def build_db():
    db.create_all()
    return 'abc'
