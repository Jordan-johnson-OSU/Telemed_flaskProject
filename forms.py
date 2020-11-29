from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired
from wtforms import Form, StringField, SelectField


class LoginForm(FlaskForm):
    name = StringField(u'Username', validators=[DataRequired()])
    password = StringField(u'Password', validators=[DataRequired()])

    submit = SubmitField(u'Login')


# added by mroyster temporarily
class IndexForm(FlaskForm):
    s1 = StringField(u'Hello', validators=[DataRequired()])
    hello = SubmitField(u'test')


# Prescription Form
class PrescriptionForm(FlaskForm):
    patientFirst = StringField(u'Patient First Name', validators=[DataRequired()])
    patientLast = StringField(u'Patient Last Name', validators=[DataRequired()])
    medication = StringField(u'Medication', validators=[DataRequired()])
    strength = IntegerField(u'Strength', validators=[DataRequired()])
    quantity = IntegerField(u'Quantity', validators=[DataRequired()])
    directions = StringField(u'Directions', validators=[DataRequired()])
    isSent = None
    create = SubmitField(u'Create')


class AllergyRecord(FlaskForm):
    # allergy
    patientFirstName = StringField(u'Patient First name')
    patientLastName = StringField(u'Patient Last name')
    allergyMedication = StringField(u'Allergic Medication')
    allergyDescription = StringField(u'Allergic Description')
    # dateEntered = DateField(u'Date Entered')
    createdBy = StringField(u'Created By')

    createAllergy = SubmitField(u'Create')


class DiagnosisRecord(FlaskForm):
    # diagnosis
    disease = StringField(u'Disease')
    condition = StringField(u'Condition')
    treatment = StringField(u'Treatment')

    createDiagnosis = SubmitField(u'Create')


class PatientRecord(FlaskForm):
    # allergy
    patientFirstName = StringField(u'Patient First name')
    patientLastName = StringField(u'Patient Last name')
    patientEmail = StringField(u'Patient Email')

    createPatient = SubmitField(u'Create')


class CreateMedicalRecord(FlaskForm):
    # DIAGNOSIS
    disease = StringField(u'Disease')
    condition = StringField(u'Condition')
    treatment = StringField(u'Treatment')
    
    # PRESCRIPTION
    scriptMedication = StringField(u'Medication')
    scriptStrength = StringField(u'Strength')
    scriptDirections = StringField(u'Directions')
        
    # DOCTOR (also gets tied to prescription class)
    doctorID = StringField(u'Doctor ID')
    doctorFirstName = StringField(u'Doctor First Name')
    doctorLastName = StringField(u'Doctor Last Name')
    doctorProvider = StringField(u'Provider')

    # PATIENT
    patientFirstName = StringField(u'Patient First name')
    patientLastName = StringField(u'Patient Last name')
    patientEmail = StringField(u'Patient Email')

    # Fields for all classes
    # date = DateTimeField(u'Date', validators=[DataRequired()])

    create = SubmitField(u'Create')


class MedicalRecordForm(FlaskForm):
    patientFirstName = StringField(u'Patient First name')
    patientLastName = StringField(u'Patient Last name')
    search = SubmitField(u'Search')

