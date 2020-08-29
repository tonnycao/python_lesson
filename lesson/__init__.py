from flask import Flask
from .util import ListConverter
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_object(os.environ['APP_CONFIG_FILE'])

app.url_map.converters['list'] = ListConverter
db = SQLAlchemy(app)

from . import views