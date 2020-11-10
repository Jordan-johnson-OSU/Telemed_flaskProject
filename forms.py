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

