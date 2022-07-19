from base64 import encode
from codecs import utf_8_encode
from flask import render_template, request, flash, redirect, url_for
import uuid
from . import bp as app
from app.blueprints.main.models import User, Pokemon
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required
from app.forms.forms import RegistrationForm, LoginForm
from app import db
from app import bcrypt




@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(public_id=str(uuid.uuid4()),
                                name=form.username.data,
                                email=form.email.data,
                                password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been created! Please login", 'success')
        return redirect(url_for('auth.login'))
    return render_template("register.html", title="Register", form=form)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()
       if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           next_page = request.args.get("next")
           return redirect(next_page) if next_page else redirect(url_for("main.home"))
       else:
        flash("Logging in was unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@app.route("/account")
@login_required
def account():
    pokemon= Pokemon.query.all()
    return render_template("account.html", title="Account", pokemon=pokemon, user=current_user)

@app.route("/new_pokemon")
def new_pokemon():
    return render_template("new_pokemon.html", title="Pokemon")


