import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app import db, bcrypt


class LoginHistory(db.Model, UserMixin):

    __tablename__ = 'login_history'

    email = db.Column(db.String(255), primary_key=True)
    ip = db.Column(db.String(255), primary_key=True)
    browser = db.Column(db.String(255), primary_key=True)
    session_duration = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, primary_key=True)


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    plan = db.Column(db.String(255))
    _password = db.Column(db.String(255))
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email


class Store(db.Model):

    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2083))
    description = db.Column(db.String)
    shopify_rank = db.Column(db.Integer)
    alexa_rank = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    daily_visitors = db.Column(db.Integer)
    fb_url = db.Column(db.String(2083))
    ig_url = db.Column(db.String(2083))
    tw_url = db.Column(db.String(2083))
    yt_url = db.Column(db.String(2083))
    title = db.Column(db.String)
    average_product_price = db.Column(db.Float)
    category = db.Column(db.String)


class Topic(db.Model):

    __tablename__ = "topic"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)


class StoreTopic(db.Model):

    __tablename__ = "store_topic"

    store_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, primary_key=True)