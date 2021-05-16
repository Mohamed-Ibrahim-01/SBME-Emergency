from flask import Blueprint, render_template

main = Blueprint(name='main', import_name=__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('/main/home.html',data="Hello Flask")

@main.route('/emergency')
def home():
    return render_template('/main/emergency.html',data="This is the emergency page")
