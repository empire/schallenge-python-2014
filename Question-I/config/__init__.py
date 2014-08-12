__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from flask import Flask, abort

def config_db(app):
    """

    :type app: Flask
    """

    if app.config.has_key('SQLALCHEMY_DATABASE_URI'):
        # No need ot generate uri (allow developer to use her uri)
        return

    def generate_sqlite_rui(config):
        return 'sqlite:///' + config['SQLITE']['path']

    def generate_general_dialect(dialect):
        def generate_uri(config):
            username = config['DB_USERNAME']
            password = config['DB_PASSWORD']
            host = config['DB_HOST']
            db = config['DB_NAME']
            return dialect + '://' + username + ':' + password + '@' + host + '/' + db
        return generate_uri


    uris_generators = {
        'sqlite': generate_sqlite_rui,
        'postgresql': generate_general_dialect('postgresql'),
        'mysql': generate_general_dialect('mysql'),
    }

    driver = app.config['DB_DRIVER']
    if not uris_generators.has_key(driver):
        print "Invalid db driver see config/app.cfg"
        abort(500)

    uri = uris_generators[driver](app.config)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.logger.info("DB URI: " + app.config['SQLALCHEMY_DATABASE_URI'])
    # import sys
    # sys.exit()