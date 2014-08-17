__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app, db
from flask import request, session, flash, url_for, redirect, render_template
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from forms import LoginForm
from models import Account, find_active_account_by_username_and_password

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account = find_active_account_by_username_and_password(form.username.data, form.password.data)
            if None != account:
                session['username'] = account.username
                flash("You login successfully")
                return redirect(url_for("home"))
            flash("Invalid username/password or your account is not enabled")

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if not session['username']:
        flash("You are not login")
    else:
        del session['username']
        flash("You are logging out")
    return redirect(url_for("home"))
