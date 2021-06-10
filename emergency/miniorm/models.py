class Doctor:
  def __init__ (self,Email,DoctorSsn, Name, Phone, Address, BirthDate, Sex
                , MainQualification, ExtraQualification, RoomNum="1"
                , ShiftPeriod="Day", doctor_to_room="1"):
    self.ExtraQualification = ExtraQualification
    self.MainQualification = MainQualification
    self.Sex = Sex
    self.BirthDate = BirthDate
    self.Address = Address
    self.Phone = Phone
    self.Name = Name
    self.DoctorSsn = DoctorSsn;
    self.Email = Email;
    self.RoomNum = RoomNum;
    self.doctor_to_room = doctor_to_room;
    self.ShiftPeriod = ShiftPeriod;

  def __repr__(self):
    return f"{self.DoctorSsn}-{self.Name}-{self.Phone}"


class Patient:
  def __init__ (self,PatientSsn, Name, Email, Phone, Address, Sex, BirthDate, PatientCase
                ,RoomNum="1", Weight="0", Disease="Unknown", Status="Unknown", room_to_patient="1"):
    self.Disease = Disease
    self.PatientCase = PatientCase
    self.BirthDate = BirthDate
    self.Weight = Weight
    self.Sex = Sex
    self.Address = Address
    self.Phone = Phone
    self.Name = Name
    self.RoomNum = RoomNum
    self.PatientSsn = PatientSsn
    self.Email = Email;
    self.room_to_patient = room_to_patient;
    self.Status = Status;

  def __repr__(self):
    return f"{self.PatientSsn}-{self.Name}-{self.Phone}"

class ContactMessage:
  def __init__ (self,Subject, Message, Name="Anonymous", Email="Anonymous"):
    self.Name = Name
    self.Email = Email
    self.Message = Message
    self.Subject = Subject

  def __repr__(self):
    return f"{self.Name}-{self.Subject}-{self.Message}"
