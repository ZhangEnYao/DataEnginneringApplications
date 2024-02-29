from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectMultipleField
from wtforms.validators import DataRequired

class FormLogin(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')