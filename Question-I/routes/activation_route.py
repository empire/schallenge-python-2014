__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app, db, generate_activation_message
from flask import request, flash, url_for, redirect, render_template, abort
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form
from forms import RegisterForm
from models import Account, find_account_by_activation_code
from integration import send_email

@app.route('/activation/account-check/<id>', methods=['GET'])
def activation_check(id):
    account = Account.query.get(id)
    if None == account:
        abort(404)
    return generate_activation_message(account)


@app.route('/activation/regenerate/<id>', methods=['GET'])
def activation_regenerate(id):
    account = Account.query.get(id)
    if None == account:
        abort(404)
    if account.is_activation_code_expired():
        account.generate_activation_code()
        db.session.commit()
    return generate_activation_message(account)

@app.route('/activation/activate/<code>', methods=['GET'])
def activation_activate(code):
    account = find_account_by_activation_code(code)

    if None == account:
        abort(404)

    if account.enabled:
        flash("Your account was enabled.")
        return redirect(url_for("home"))


    if account.is_activation_code_expired():
        return render_template('activation_code_expired.html', account=account)
    account.activate()
    db.session.commit()
    flash("Your account is enabled.")
    return redirect(url_for("home"))
