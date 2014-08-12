__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from flask import render_template
from lib import app
from lib.database import check_db

@app.route('/check-db', methods=['GET'])
def check_db():
    from lib.database import check_db
    if check_db():
        return render_template('check_db/success.html')
    return render_template('check_db/error.html')

