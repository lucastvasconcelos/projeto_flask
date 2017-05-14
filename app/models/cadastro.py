from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):

    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    password_test = PasswordField("password_test",validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
