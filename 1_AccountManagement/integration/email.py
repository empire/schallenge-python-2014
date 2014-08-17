__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from lib import app

def send_email(to, content):
    app.logger.info('SEND EMAIL TO: ' + to)
    app.logger.info('SEND EMAIL Content: ' + content)
    pass
