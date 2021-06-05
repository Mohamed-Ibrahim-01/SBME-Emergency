from flask import Blueprint, render_template, url_for, redirect, flash
from emergency.forms.patients import PatientForm
from emergency.miniorm.miniorm import miniorm as db
import datetime

emergency = Blueprint(name='emergency', import_name=__name__, url_prefix="/emergency")
currDate = datetime.datetime.now()
stopDate = datetime.datetime(currDate.year, currDate.month -3, currDate.day)

@emergency.route('/overview')
def overview():
    return render_template('/room/overview.html',data="This is the emergency page")

@emergency.route('/<int:roomNum>')
def room(roomNum):
    db.getEmergency(roomNum, stopDate)
    return render_template('/room/emergencyRooms.html',data="This is the emergency page")

@emergency.route('/addPatient', methods=['GET','POST'])
def addPatient():
    form = PatientForm()
    if form.validate_on_submit():
        print("\n\n",form.Name.data,form.Address.data,form.Case.data,"\n\n")
        return redirect(url_for('main.home'))
    return render_template('/patient/addPatient.html',form=form)
