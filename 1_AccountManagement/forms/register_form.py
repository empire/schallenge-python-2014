__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from wtforms_alchemy import ModelForm
from wtforms.fields import StringField, PasswordField
from wtforms import validators
from models import Account

class RegisterForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['activation_code', 'salt', 'registered_at', 'activation_code_generated_at', 'enabled', 'enabled_at']
