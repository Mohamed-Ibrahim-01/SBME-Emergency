from flask_wtf import FlaskForm,Form
from wtforms import StringField, SubmitField
from wtforms.validators import EqualTo, Length, Email, DataRequired, ValidationError
from wtforms.widgets import TextArea

class ContactUsForm(FlaskForm):
    Name = StringField("Name")
    Subject = StringField("Subject",validators=[DataRequired(),Length(min=5,max=50)])
    Mail = StringField('Email')
    Message = StringField('Message', widget=TextArea()
                          , validators=[DataRequired(),Length(min=10,max=1000)])

    Submit = SubmitField('Submit')
