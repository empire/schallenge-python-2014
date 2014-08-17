__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

import uuid
import hashlib

def check_password(hashed_password, salt, user_password):
    return hashed_password == hash_password(salt, user_password)

def hash_password(salt, password):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def generate_random_activation_code():
    return uuid.uuid4().hex

def generate_salt():
    return uuid.uuid4().hex
