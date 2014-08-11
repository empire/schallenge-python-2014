from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
from flask_sqlalchemy import SQLAlchemy

import uuid
import hashlib

app = Flask(__name__)
app.config.from_pyfile('config/app.cfg')
db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.Boolean)
    email = db.Column(db.String(200))
    password = db.Column(db.String)
    salt = db.Column(db.String(200))
    registered_at = db.Column(db.DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.registered_at = datetime.utcnow()
        self.salt = uuid.uuid4().hex

    def __hash_password(salt, password):
        # uuid is used to generate a random number
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    def __check_password(password, salt, user_password):
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


@app.route('/')
def show_all():
    return render_template('show_all.html',
        todos=Account.query.order_by(Account.registered_at.desc()).all()
    )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')


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

if __name__ == '__main__':
    app.run()
