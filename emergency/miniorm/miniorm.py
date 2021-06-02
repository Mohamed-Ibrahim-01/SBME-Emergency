import emergency
import mysql.connector, json
from emergency.miniorm.models import *
from emergency.config import Config

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd= Config.DB_PASS,
  database="emergency",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

class miniorm:

    def getAllDoctor():
        mycursor.execute("SELECT * FROM Doctor")
        fetchedDoctors = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        doctors = [ Doctor(**dict(zip(row_headers,doctor))) for doctor in fetchedDoctors ]

        return doctors

    def getAllPatient():
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


