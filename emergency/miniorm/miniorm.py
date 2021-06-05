import mysql.connector
from emergency.miniorm.models import *
from flask import current_app

mydb = mysql.connector.connect(
    host=current_app.config['DB_HOST'],
    user=current_app.config['DB_USER'],
    passwd= current_app.config['DB_PASS'],
    database=current_app.config['DB_NAME'],
    auth_plugin=current_app.config['DB_AUTH']
)

mycursor = mydb.cursor()

class miniorm:

    def getAllDoctor(self):
        mycursor.execute("SELECT * FROM Doctor")
        fetchedDoctors = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        doctors = [ Doctor(**dict(zip(row_headers,doctor))) for doctor in fetchedDoctors ]

        return doctors

    def getAllPatient(self):
        mycursor.execute("SELECT * FROM Patient")
        fetchedPatients = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        patients = [ Patient(**dict( zip(row_headers,patient) )) for patient in fetchedPatients ]

        return patients;

    def getNumOf(tableName):
        return 0
    def getAccount(email, password):
        return 0
    def getEmergency(emergencyNumber, endDate):
        return 0


