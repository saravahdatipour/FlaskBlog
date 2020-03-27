  
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])



class RegisterForm(FlaskForm):
    conpass = PasswordField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    full_name = StringField()
    email = EmailField(validators=[DataRequired()])
#     password = PasswordField(validators=[DataRequired()])
#     confirmpassword = PasswordField(validators=[DataRequired()])


