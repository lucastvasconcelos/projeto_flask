from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):

    username = StringField("username",validators=[DataRequired()])
    password = StringField("password",validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
