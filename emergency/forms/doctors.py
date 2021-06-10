from flask_wtf import FlaskForm,Form
from wtforms import StringField, SubmitField
from wtforms.validators import EqualTo, Length, Email, DataRequired, ValidationError, Regexp

class DoctorForm(FlaskForm):
    Ssn = StringField("Ssn",validators=[DataRequired(),Length(min=14,max=14)])
    Name = StringField("Name",validators=[DataRequired(),Length(min=2,max=50)])

    Phone = StringField("Phone",validators=[DataRequired(),Regexp("01[0-9]{9}",
                        message="Write a valid EG phone number")])

    BirthDate = StringField("BirthDate",validators=[DataRequired(),
                            Regexp("[0-9]{2}\\/[0-9]{2}\\/[1|2][0-9]{3}",
                            message="Birth Date must be in format dd/mm/yyyy")])

    Address = StringField("Address",validators=[DataRequired(),Length(min=4,max=50)])
    Sex = StringField("Sex",validators=[DataRequired(),Length(min=4,max=6)])
    MainQualification = StringField("Main Qualification",validators=[DataRequired(),Length(min=6,max=50)])
    ExtraQualification = StringField("Extra Qualification",validators=[DataRequired(),Length(min=4,max=50)])
    Mail = StringField('Email', validators=[DataRequired(), Email()])
    RoomNum = StringField('Room Num', validators=[DataRequired()])

    Submit = SubmitField('Add')
