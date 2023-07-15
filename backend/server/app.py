from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from configparser import ConfigParser

from marshmallow import ValidationError

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

config = ConfigParser()

config.optionxform = str
config.read('config.ini')
app.config.update(dict(config['flask']))

db.init_app(app)
migrate.init_app(app)
ma.init_app(app)
cors.init_app(app)


@app.errorhandler(ValidationError)
def register_validation_error(error):
    rv = dict({
        'message': 'body-validation',
        'errors': error.messages
    })
    return rv, 400


import server.routes
