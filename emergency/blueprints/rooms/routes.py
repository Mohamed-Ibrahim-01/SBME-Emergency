
from flask import Blueprint, render_template

emergency = Blueprint(name='main', import_name=__name__)

@emergency.route('/emergency')
def home():
    return render_template('/main/emergency.html',data="This is the emergency page")