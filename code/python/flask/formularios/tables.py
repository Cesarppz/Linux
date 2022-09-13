from wtforms import  Form, StringField, HiddenField, PasswordField
from wtforms.fields import EmailField

from wtforms import validators

from models import User

def length_hp(form, field):
    if field.data == None:
        pass
    elif len(field.data) > 0:
        raise validators.ValidationError('Error ')


class CommentForm(Form):
    comment     = StringField('Comment')
    honeypot    = HiddenField('Honeypot', [length_hp])


class LoginForm(Form):
    username    = StringField('Username', [validators.length(min=4, max=25, message='Please enter a valid username')])
    password    = PasswordField('Password', [validators.DataRequired()])
    email       = EmailField('Email', [validators.DataRequired(), validators.Email(message='Please enter a valid email')])

    def validate_username(form, field):
        username = field.data 
        user = User.query.filter_by(name=username).first()
        if user is not None:            
            raise validators.ValidationError('Error el usuario ya se encuetra registrado') 

class SignupForm(Form):
    username    = StringField('Username', [validators.length(min=4, max=25, message='Please enter a valid username')])
    password    = PasswordField('Password', [validators.DataRequired()])

