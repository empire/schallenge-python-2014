__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app, db, generate_activation_message
from flask import request, flash, url_for, redirect, render_template
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from forms import RegisterForm
from models import Account
from integration import send_email

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        account = Account()
        if form.validate():
            form.populate_obj(account)
            db.session.add(account)
            db.session.commit()

            send_email(account.email, generate_activation_message(account))

            flash("You are registered successfully")
            return redirect(url_for("home"))

    return render_template('register.html', form=form)
