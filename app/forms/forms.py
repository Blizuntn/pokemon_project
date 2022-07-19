from flask_wtf import FlaskForm
from marshmallow import ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.blueprints.main.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password= PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit= SubmitField("Register")
    
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError("That username is taken. Please choose another username.")
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError("That email is taken. Please choose another email.")
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit= SubmitField("Login")
    
class PokemonForm(FlaskForm):
    pokemon_name= StringField("Name", validators=[DataRequired()])
    pokemon_type= StringField("Type", validators=[DataRequired()])
    pokemon_description= TextAreaField("Description", validators=[DataRequired()])
    submit= SubmitField("Collect")