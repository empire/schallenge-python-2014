__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from wtforms import Form, PasswordField, StringField, validators

class LoginForm(Form):
    username = StringField(u'Username', validators=[validators.input_required()])
    password = StringField(u'Password', validators=[validators.input_required()])
