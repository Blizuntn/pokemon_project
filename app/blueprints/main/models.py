from app import db, login_manager
from flask_login import UserMixin
from flask import Flask, flash, request
from datetime import datetime
from enum import unique
from sqlalchemy import UniqueConstraint

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __table_args__ = (db.UniqueConstraint('public_id', "email"),)
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(250),unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    character = db.relationship("Pokemon", backref="user", lazy="dynamic")


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    type_ = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.Column(db.String(250), db.ForeignKey("user.public_id"))
