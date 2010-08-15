import logging
import os

from flask import Flask, g
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

logging.basicConfig(level=logging.DEBUG)

HOST = "localhost"
app = Flask(__name__)
db = SQLAlchemy(app)
md = Markdown(app, extensions=['tables'])

from .utils import register_modules
from .views.admin import admin
from .views.events import events
from .views.meetings import meetings
from .views.pages import pages

register_modules(app, [admin, events, meetings, pages])

app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# see if the db exists, if not make it and initialize
if not os.path.exists(app.config.get('SQLALCHEMY_DATABASE_URI')):
    db.create_all()


def update_config():
    """syncronizes the config with the g global request object"""
    g.config = app.config

app.before_request(update_config)
