import os
import flask
from flask import render_template, url_for, request, redirect, flash
from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, Subgroup, Link
from flask_sqlalchemy import SQLAlchemy
from forms import *
# from models import *
from nav import nav

# Init some things
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='superdupersupersecret',
    DATABASE=os.path.join(app.instance_path, 'telemedicine.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# login_manager = LoginManager()
# login_manager.init_app(app)

AppConfig(app)
Bootstrap(app)

# build the navigation
nav.register_element('frontend_top', Navbar(
    Link('Login', 'login'),
    Link('Home', 'home'),
    Subgroup(
        'Appointments',
        Link('Create Appointment', 'home'),
        Link('View Past Appointments', 'home'),
        Link('Join Appointment', 'home'), ),
    Subgroup(
        'Medical Records',
        Link('My Medical Records', 'list'),
        Link('Create New', 'new'),
        Link('Find Patient Medical Records', 'medicalRecord/search'), ),
    Subgroup(
        'Payments',
        Link('My Payment Records', 'home'),
        Link('Make Payment', 'home'), ),
    Subgroup(
        'Prescriptions',
        Link('My Prescriptions', 'prescriptionList'),
        Link('Pending Prescription', 'home'),
        Link('New Prescription', 'newPrescription'), ),
))

nav.init_app(app)

# Creating a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/telemedicine.db'
db = SQLAlchemy(app)

from models import *

# we may want ot drop it and create it every time for testing
db.drop_all()
db.create_all()

#
# @login_manager.user_loader
# def load_user(user_id):
#    return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    # user = User.query.all()
    # print(user.user_id)

    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of `User` class
        # login_user(user)

        return flask.redirect(flask.request.args.get('next') or flask.url_for('home'))
    return flask.render_template('index.html', form=form)


@app.route("/logout")
# @login_required
def logout():
    # do logout
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


# Added by RoperFV, found on Flask 101
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Added by RoperFV, found on Flask 101
@app.route('/medicalRecord/search')
def search_medical_records():
    search = MedicalRecordForm()
    if request.method == 'POST':
        results = []
        search_string = search.data['search']
        if search.data['search'] == '':
            qry = db.session.query('PatientLast')
            results = qry.all()
        if not results:
            flash('No results found!')
            return redirect('/list')
        else:
            # display results
            return render_template('recordSearch.html', results=results)

    return render_template('recordSearch.html', form=search)


@app.route('/list')
def list_medical_records():
    diagnosis = Diagnosis.query.order_by(Diagnosis.disease).all()
    patients = Patient.query.order_by(Patient.first_name).all()
    allergies = Allergy.query.order_by(Allergy.allergyMedication).all()
    return render_template('recordList.html',
                           diagnosis=diagnosis,
                           patients=patients,
                           allergies=allergies)


@app.route('/new', methods=['GET', 'POST'])
def create_medical_record():
    # form = CreateMedicalRecord()
    diagnosisForm = DiagnosisRecord()
    patientForm = PatientRecord()
    allergyForm = AllergyRecord()

    if request.method == 'POST':
        if diagnosisForm.createDiagnosis.data:
            print("diagnosisForm Is Submitted ", diagnosisForm.createDiagnosis.data)
            if diagnosisForm.validate_on_submit():
                    record = Diagnosis(disease=diagnosisForm.disease.data,
                                       condition=diagnosisForm.condition.data,
                                       treatment=diagnosisForm.treatment.data)
                    try:
                        db.session.add(record)
                        db.session.commit()
                        return redirect('/list')
                    except:
                        print("ERROR Diagnosis Record Creation")
                        return 'There was an error with the database'

        elif patientForm.createPatient.data:
            print("patientForm Is Submitted ", patientForm.createPatient.data)
            if patientForm.validate_on_submit():
                    record = Patient(first_name=patientForm.patientFirstName.data,
                                     last_name=patientForm.patientLastName.data,
                                     email=patientForm.patientEmail.data)
                    try:
                        db.session.add(record)
                        db.session.commit()
                        return redirect('/list')
                    except:
                        print("ERROR Patient Record Creation")
                        return 'There was an error with the database'

        elif allergyForm.createAllergy.data:
            print("allergyForm Is Submitted ", allergyForm.createAllergy.data)
            if allergyForm.validate_on_submit():
                    record = Allergy(patientFirstName=allergyForm.patientFirstName.data,
                                     patientLastName=allergyForm.patientLastName.data,
                                     allergyMedication=allergyForm.allergyMedication.data,
                                     allergyDescription=allergyForm.allergyDescription.data,
                                     # dateEntered=allergyForm.dateEntered.data,
                                     createdBy=allergyForm.createdBy.data)

                    try:
                        db.session.add(record)
                        db.session.commit()
                        print("Allergy created")
                        return redirect('/list')
                    except:
                        print("ERROR Allergy Record Creation")
                        return 'There was an error with the database'
    else:
        return render_template('recordForm.html',
                               diagnosisForm=diagnosisForm,
                               patientForm=patientForm,
                               allergyForm=allergyForm)
    return redirect('/home')


@app.route('/newPrescription', methods=['GET', 'POST'])
def create_prescription():
    form = PrescriptionForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            prescription = Prescription(patientFirst=form.patientFirst.data,
                                        patientLast=form.patientLast.data,
                                        medication=form.medication.data,
                                        strength=form.strength.data,
                                        quantity=form.quantity.data,
                                        directions=form.directions.data)
        try:
            db.session.add(prescription)
            db.session.commit()
            return redirect('/prescriptionList')
        except:
            return 'There was an error adding the prescription to the database'
    else:
        return render_template('prescriptionForm.html', form=form)


@app.route('/prescriptionList')
def list_prescriptions():
    prescriptions = Prescription.query.order_by(Prescription.patientFirst).all()
    return render_template('prescriptionList.html', prescriptions=prescriptions)


@app.route('/medicalRecord/<record>')
def show_medical_record(record):
    print('Medical Record  %s' % record)
    return render_template('recordList.html')


if __name__ == "__main__":
    app.run(debug=True)
