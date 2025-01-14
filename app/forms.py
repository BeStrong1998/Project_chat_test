from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class MainPage(FlaskForm):
    submit_exit = SubmitField('Выйти')


class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
  username = StringField('Имя', validators=[DataRequired()])
  email = StringField('Почта', validators=[DataRequired(), Email()])
  password = PasswordField('Пароль', validators=[DataRequired()])
  password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Зарегистрироваться')


  def validate_username(self, username):
    user = db.session.scalar(sa.select(User).where(User.username == username.data))
    if user is not None:
      raise ValidationError('Пожалуйста, используйте другое имя пользователя.')

  def validate_email(self, email):
    user = db.session.scalar(sa.select(User).where(User.email == email.data))
    if user is not None:
      raise ValidationError('Пожалуйста, используйте другой адрес электронной почты.')