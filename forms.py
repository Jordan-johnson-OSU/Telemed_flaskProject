from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired
from wtforms import Form, StringField, SelectField


class LoginForm(FlaskForm):
    name = StringField(u'Username', validators=[DataRequired()])
    password = StringField(u'Password', validators=[DataRequired()])

    submit = SubmitField(u'Login')


# Temporarily disabled by RoperFV

#class MedicalRecordForm(FlaskForm):
    #a_float = FloatField(u'A floating point number')
    #a_decimal = DecimalField(u'Another floating point number')
    #a_integer = IntegerField(u'An integer')
   # now = DateTimeField(u'Current time', description='...for no particular reason')
   # sample_file = FileField(u'Your favorite file')
   # eula = BooleanField(u'I did not read the terms and conditions',
   #                     validators=[DataRequired('You must agree to not agree!')])
   # submit = SubmitField(u'Submit')

## added by mroyster temporarily
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
    # Saved for later
    # sentToPharmacy = StringField(u'Hello', validators=[DataRequired()])
    create = SubmitField(u'Create')

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


class MedicalRecordForm(Form):
    choices = [('PatientLast', 'PatientFirst'),
               ('Prescription', 'Strength'),
               ('Condition', 'Diagnoses')]
    select = SelectField('Search for records:', choices=choices)
    search = StringField('')