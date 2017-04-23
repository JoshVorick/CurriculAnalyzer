from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class classForm(Form):
    dept = StringField('dept', validators=[DataRequired()])
    subNumber = StringField('subNumber', validators=[DataRequired()])
    
    