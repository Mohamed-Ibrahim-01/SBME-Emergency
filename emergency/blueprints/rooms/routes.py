from flask import Blueprint, render_template, url_for, redirect
from emergency.forms.patients import PatientForm
from emergency.forms.doctors import DoctorForm
from emergency.miniorm.miniorm import miniorm
from emergency.miniorm.models import *
import datetime

emergency = Blueprint(name='emergency', import_name=__name__, url_prefix="/emergency")
currDate = datetime.datetime.now()
stopDate = datetime.datetime(currDate.year, currDate.month -3, currDate.day)
db = miniorm()

@emergency.route('/overview')
def overview():
    doctors = db.getAllDoctors()
    patients = db.getAllPatients()
    return render_template('/room/overview.html',data={ "doctors": doctors, "patients": patients})

@emergency.route('/<int:roomNum>')
def room(roomNum):
    return render_template('/room/emergencyRooms.html',data="This is the emergency page")

@emergency.route('/addPatient', methods=['GET','POST'])
def addPatient():
    form = PatientForm()
    if form.validate_on_submit():
      newPatient= Patient(
        Email=form.Mail.data,
        PatientSsn=form.Ssn.data,
        Name=form.Name.data,
        Phone=form.Phone.data,
        Sex=form.Sex.data,
        BirthDate=form.BirthDate.data,
        PatientCase=form.Case.data,
        RoomNum="1",
        Address=form.Address.data
      )
      db.addPatient(newPatient)
      return redirect(url_for('emergency.overview'))
    return render_template('/patient/addPatient.html',form=form)

@emergency.route('/addDoctor', methods=['GET','POST'])
def addDoctor():
    form = DoctorForm()
    print (form.validate_on_submit())
    if form.validate_on_submit():
        newDoctor= Doctor(
          Email=form.Mail.data,
          DoctorSsn=form.Ssn.data,
          Name=form.Name.data,
          Phone=form.Phone.data,
          Sex=form.Sex.data,
          BirthDate=form.BirthDate.data,
          MainQualification=form.MainQualification.data,
          ExtraQualification=form.ExtraQualification.data,
          RoomNum="1",
          Address=form.Address.data
        )
        db.addDoctor(newDoctor)
        return redirect(url_for('emergency.overview'))
    return render_template('/doctor/addDoctor.html',form=form)
