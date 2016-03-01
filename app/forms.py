import random
from random import randint
from flask.ext.wtf import Form
from wtforms.fields import TextField, FileField,IntegerField,SelectField,SubmitField
from wtforms.validators import Required,ValidationError
from flask_wtf.file import FileField,FileAllowed,FileRequired

class myform(Form):
    image = FileField('Image File', validators=[FileRequired(),FileAllowed(['jpg','jpeg' 'png'], 'Images only!')])
    firstname = TextField('First Name',validators=[Required()])
    lastname = TextField('Last Name',validators=[Required()])
    age = TextField('Age',validators=[Required()])
    sex = SelectField('Sex', validators=[Required()], choices=[('male','Male'),('female','Female'),('other','Other')])
    #user = SubmitField('add user')
  
"""
    def validate_fname(self,form, field):
        if len(field.data) > 15:
            raise ValidationError('Name must be less than 15 characters')
   
    def validate_lname(self,form, field):
        if len(field.data) > 25:
            raise ValidationError('Name must be less than 50 characters')
    
    def validate_age(self,form, field):
        if len(field.data) > 3:
            raise ValidationError('Age must be less than 3 characters')
"""