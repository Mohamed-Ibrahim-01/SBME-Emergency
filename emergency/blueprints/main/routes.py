from flask import Blueprint, render_template, url_for, redirect
from emergency.forms.contactUs import ContactUsForm
from emergency.miniorm.miniorm import miniorm
from emergency.miniorm.models import *
main = Blueprint(name='main', import_name=__name__)
db = miniorm()

@main.route('/')
@main.route('/home')
def home():
    return render_template('/main/home.html',data="Hello Flask")

@main.route('/contactUs',methods=['GET','POST'])
def contactUs():
    form = ContactUsForm()
    if form.validate_on_submit():
        newMessage= ContactMessage(
            Name = form.Name.data if form.Name.data else "Anonymous",
            Subject = form.Subject.data,
            Email = form.Mail.data if form.Name.data else "Anonymous",
            Message = form.Message.data
        )
        db.addContactMessage(newMessage)
        return redirect(url_for('main.contactUsResponses'))
    return render_template('/main/contactUs.html',form=form)

@main.route('/contactUs/responses')
def contactUsResponses():
    messages = db.getAllMessages()
    return render_template('/main/contactUsResponses.html',messages=messages)
