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


class miniorm:

    def addDoctor(self,doctor):
      mycursor = mydb.cursor()
      mycursor.execute(
        """INSERT INTO Doctor (
        DoctorSsn, Name, Phone, Address, BirthDate, Sex, MainQualification
        , ExtraQualification, Email, doctor_to_room, ShiftPeriod)VALUES(
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        ,(doctor.DoctorSsn, doctor.Name, doctor.Phone, doctor.Address, doctor.BirthDate
          , doctor.Sex, doctor.MainQualification, doctor.ExtraQualification , doctor.Email
          , doctor.RoomNum, doctor.ShiftPeriod)
      )
      mydb.commit()
      mycursor.close()

    def addPatient(self,patient):
      mycursor = mydb.cursor()
      mycursor.execute(
        """INSERT INTO Patient (PatientSsn, Name, Phone, Address, Sex, PatientCase
        , room_to_patient, BirthDate, Email) VALUES(
        %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        ,(patient.PatientSsn, patient.Name, patient.Phone, patient.Address, patient.Sex
          , patient.PatientCase , patient.RoomNum, patient.BirthDate, patient.Email)
      )
      mydb.commit()
      mycursor.close()

    def addContactMessage(self, message):
      mycursor = mydb.cursor()
      mycursor.execute(
        """INSERT INTO ContactUs (Name, Subject, Email, Message) VALUES( %s,%s,%s,%s)"""
        ,(message.Name, message.Subject, message.Email, message.Message)
      )
      mydb.commit()
      mycursor.close()

    def getAllDoctors(self):
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM Doctor")
      fetchedDoctors = mycursor.fetchall()
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      doctors = [ Doctor(**dict(zip(row_headers,doctor))) for doctor in fetchedDoctors ]

      mycursor.close()
      return doctors

    def getAllPatients(self):
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM Patient")
      fetchedPatients = mycursor.fetchall()
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      patients = [ Patient(**dict( zip(row_headers,patient) )) for patient in fetchedPatients ]

      mycursor.close()
      return patients

    def getAllMessages(self):
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM ContactUs")
      fetchedMessages = mycursor.fetchall()
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      messages = [ ContactMessage(**dict( zip(row_headers,message) )) for message in fetchedMessages ]

      mycursor.close()
      return messages

