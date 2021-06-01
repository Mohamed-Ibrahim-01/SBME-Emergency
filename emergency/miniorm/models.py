
class Doctor:
  def __init__ (self,DoctorSsn, Name, Phone, Address, BirthDate, Sex, MainQualification, ExtraQualification,doctor_to_account,doctor_to_room,ShiftPeriod):
    self.doctor_to_room = doctor_to_room
    self.doctor_to_account = doctor_to_account
    self.ExtraQualification = ExtraQualification
    self.MainQualification = MainQualification
    self.Sex = Sex
    self.BirthDate = BirthDate
    self.Address = Address
    self.Phone = Phone
    self.Name = Name
    self.DoctorSsn = DoctorSsn;

  def __repr__(self):
    return f"Doc :: {self.DoctorSsn},{self.Name},{self.Phone},{self.Sex},{self.Address},{self.MainQualification}"

class Patient:
  def __init__ (self,PatientSsn, Name, Phone, Address, Sex, Weight, BirthDate, Status, PatientCase, Disease,room_to_patient,EnteringDate):
    self.Disease = Disease
    self.PatientCase = PatientCase
    self.Status = Status
    self.BirthDate = BirthDate
    self.Weight = Weight
    self.Sex = Sex
    self.Address = Address
    self.Phone = Phone
    self.Name = Name
    self.PatientSsn = PatientSsn

  def __repr__(self):
    return f"Patient :: {self.PatientSsn},{self.Name},{self.Phone},{self.Sex},{self.Address},{self.MainQualification}"