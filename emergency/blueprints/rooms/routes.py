from flask import Blueprint, render_template
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
