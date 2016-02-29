import random
from random import randint
from flask .ext.wtf import form
from wtforms.fields import TextField, FileField,IntegerField
from wtforms.validators import Required

class myform(form)
    image = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
    fname = TextField('fname',validators=[Required()]])
    lname = TextField('lname',validators=[Required()])
    age = TextField('age',validators=[Required()])
    sex = SelectField('Sex', validators= [Required(), choice=[(1,'male'),(2,'female'),(3,'other')]])
    add_user = SubmitField('add user')
    
    def validate_fname(form, field):
        if len(field.data) > 15:
            raise ValidationError('Name must be less than 15 characters')
   
    def validate_lname(form, field):
        if len(field.data) > 25:
            raise ValidationError('Name must be less than 50 characters')
    
    def validate_age(form, field):
        if len(field.data) > 3:
            raise ValidationError('Age must be less than 3 characters')
    
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)
