__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from flask import render_template

def generate_activation_message(account):
    return render_template('email_activation.html', account=account)
