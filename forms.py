from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired


class LoginForm(FlaskForm):
    name = StringField(u'Username', validators=[DataRequired()])
    password = StringField(u'Password', validators=[DataRequired()])

    submit = SubmitField(u'Login')


class MedicalRecordForm(FlaskForm):
    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time', description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[DataRequired('You must agree to not agree!')])

    submit = SubmitField(u'Submit')

## added by mroyster temporarily
class IndexForm(FlaskForm):
    hello = SubmitField(u'test')

class CreateMedicalRecord(FlaskForm):
    # Fields for Diagnosis
    disease = StringField(u'Disease', validators=[DataRequired()])
    condition = StringField(u'Condition', validators=[DataRequired()])
    treatment = StringField(u'Treatment', validators=[DataRequired()])
    
    # Fields for prescription class
    scriptMedication = StringField(u'Medication', validators=[DataRequired()])
    scriptStrength = StringField(u'Strength', validators=[DataRequired()])
    scriptDirections = StringField(u'Directions', validators=[DataRequired()])
        
    # Fields for doctor class (also gets tied to prescription class)
    doctorID = StringField(u'Doctor ID', validators=[DataRequired()])
    doctorFirstName = StringField(u'Doctor First Name', validators=[DataRequired()])
    doctorLastName = StringField(u'Doctor Last Name', validators=[DataRequired()])
    doctorProvider = StringField(u'Provider', validators=[DataRequired()])

    # Fields for patient class
    patientFirstName = StringField(u'Patient First name', validators=[DataRequired()])
    patientLastName = StringField(u'Patient Last name', validators=[DataRequired()])
    patientEmail = StringField(u'Patient Email', validators=[DataRequired()])

    # Fields for all classes
    # date = DateTimeField(u'Date', validators=[DataRequired()])

    create = SubmitField(u'Create')