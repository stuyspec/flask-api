from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix


flask_api = Flask(__name__)

flask_api.wsgi_app = ProxyFix(flask_api.wsgi_app)

flask_api.config.from_object('config')

db = SQLAlchemy(flask_api)

import views


