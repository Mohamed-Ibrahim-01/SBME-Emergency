from flask import Blueprint, render_template

main = Blueprint(name='main', import_name=__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('/main/home.html',data="Hello Flask")

@main.route('/login')
def login():
    return render_template('/main/login.html',data="Login Page")

