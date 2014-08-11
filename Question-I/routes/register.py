__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app, db
from flask import request, flash, url_for, redirect, render_template
from wtforms import validators
from flask_wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from models import Account

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        AccountForm = model_form(Account, Form)
        form = AccountForm(request.form)
        account = Account()
        if form.validate():
            print vars(account)
            form.populate_obj(account)
            print vars(account)
            db.session.add(account)
            db.session.commit()

            flash("Success")
            return redirect(url_for("home"))

        if not request.form['username']:
            flash('Title is required', 'error')
        elif not request.form['password']:
            flash('Text is required', 'error')
        elif not request.form['email']:
            flash('Text is required', 'error')
        else:
            pass

            # todo = Todo(request.form['title'], request.form['text'])
            # db.session.add(todo)
            # db.session.commit()
            # flash(u'Todo item was successfully created')
            # return redirect(url_for('show_all'))
    return render_template('register.html')
