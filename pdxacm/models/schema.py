# Schema goes here

from werkzeug import generate_password_hash, check_password_hash
from pdxacm.webapp import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))
    email = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    # permissions = db.Column(db.Integer)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def set_permissions(self, permissions):
        pass

    def __repr__(self):
        return '<User %r>' % self.username


class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    text = db.Column(db.String)
    last_edited_on = db.Column(db.DateTime, onupdate=(datetime.today))
    last_edited_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    frozen = db.Column(db.Boolean, default=False)
    edited_by = db.relationship('User',
                                order_by=User.id,
                                backref='users')


class Group(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    permissions = db.Column(db.Integer)
