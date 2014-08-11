__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app, db
from flask import request, flash, url_for, redirect, render_template
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from forms import RegisterForm
from models import Account

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        account = Account()
        if form.validate():
            form.populate_obj(account)
            db.session.add(account)
            db.session.commit()

            flash("Success")
            return redirect(url_for("home"))
    return render_template('register.html', form=form)
