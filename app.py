import os

import flask
from flask import Flask
from flask import render_template, request, redirect
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
    Link('Login', '/login'),
    Link('Home', '/home'),
    Subgroup(
        'Appointments',
        Link('Create Appointment', '/home'),
        Link('View Past Appointments', '/home'),
        Link('Join Appointment', '/home'), ),
    Subgroup(
        'Medical Records',
        Link('My Medical Records', '/list'),
        Link('Create New', '/new'),
        Link('Find Patient Medical Records', '/medicalRecord/search'), ),
    Subgroup(
        'Payments',
        Link('My Payment Records', '/home'),
        Link('Make Payment', '/home'), ),
    Subgroup(
        'Prescriptions',
        Link('My Prescriptions', '/prescriptionList'),
        Link('Pending Prescription', '/home'),
        Link('New Prescription', '/newPrescription'), ),
))

nav.init_app(app)

# Creating a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/telemedicine.db'
db = SQLAlchemy(app)

from models import *


# we may want to drop it and create it every time for testing
# db.drop_all()
# db.create_all()

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
@app.route('/medicalRecord/search', methods=['GET'])
def search_medical_records():
    form = MedicalRecordForm()

    return render_template('recordSearch.html', form=form)


@app.route('/medicalRecord/search', methods=['POST'])
def medical_records_search_list():
    search = MedicalRecordForm()

    if search.search.data:
        if search.validate_on_submit():
            first = search.patientFirstName.data
            last = search.patientLastName.data

            # diagnosis = Diagnosis.query.order_by(Diagnosis.disease)
            # patients = Patient.query.order_by(Patient.first_name)
            # allergies = Allergy.query.order_by(Allergy.allergyMedication)

            diagnosis = db.session.query(Diagnosis)
            patients = db.session.query(Patient)
            allergies = db.session.query(Allergy)

            if first:
                print('First ', first)
                # diagnosis = diagnosis.filter(Allergy.patientFirstName == first)
                patients = patients.filter(Patient.first_name == first)
                allergies = allergies.filter(Allergy.patientFirstName == first)

            if last:
                print('Last ', last)
                # diagnosis = diagnosis.filter(Diagnosis. == last)
                patients = patients.filter(Patient.last_name == last)
                allergies = allergies.filter(Allergy.patientLastName == last)

            return render_template('recordList.html',
                                   diagnosis=diagnosis.all(),
                                   patients=patients.all(),
                                   allergies=allergies.all())

    return render_template('recordSearch.html', form=search)


@app.route('/list')
def list_medical_records():
    diagnosis = db.session.query(Diagnosis).order_by(Diagnosis.disease).all()
    patients = db.session.query(Patient).order_by(Patient.first_name).all()
    allergies = db.session.query(Allergy).order_by(Allergy.allergyMedication).all()
    return render_template('recordList.html',
                           diagnosis=diagnosis,
                           patients=patients,
                           allergies=allergies)


@app.route('/new', methods=['GET', 'POST'])
def create_medical_record():
    # form = CreateMedicalRecord()
    diagnosis_form = DiagnosisRecord()
    patient_form = PatientRecord()
    allergy_form = AllergyRecord()

    if request.method == 'POST':
        if diagnosis_form.createDiagnosis.data:
            print("diagnosis_form Is Submitted ", diagnosis_form.createDiagnosis.data)
            if diagnosis_form.validate_on_submit():
                record = Diagnosis(disease=diagnosis_form.disease.data,
                                   condition=diagnosis_form.condition.data,
                                   treatment=diagnosis_form.treatment.data)
                try:
                    db.session.add(record)
                    db.session.commit()
                    return redirect('/list')
                except:
                    print("ERROR Diagnosis Record Creation")
                    return 'There was an error with the database'

        elif patient_form.createPatient.data:
            print("patient_form Is Submitted ", patient_form.createPatient.data)
            if patient_form.validate_on_submit():
                record = Patient(first_name=patient_form.patientFirstName.data,
                                 last_name=patient_form.patientLastName.data,
                                 email=patient_form.patientEmail.data)
                try:
                    db.session.add(record)
                    db.session.commit()
                    return redirect('/list')
                except:
                    print("ERROR Patient Record Creation")
                    return 'There was an error with the database'

        elif allergy_form.createAllergy.data:
            print("allergy_form Is Submitted ", allergy_form.createAllergy.data)
            if allergy_form.validate_on_submit():
                record = Allergy(patientFirstName=allergy_form.patientFirstName.data,
                                 patientLastName=allergy_form.patientLastName.data,
                                 allergyMedication=allergy_form.allergyMedication.data,
                                 allergyDescription=allergy_form.allergyDescription.data,
                                 # dateEntered=allergyForm.dateEntered.data,
                                 createdBy=allergy_form.createdBy.data)

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
                               diagnosisForm=diagnosis_form,
                               patientForm=patient_form,
                               allergyForm=allergy_form)
    return redirect('/home')


@app.route('/newPrescription', methods=['GET', 'POST'])
def create_prescription():
    prescription = Prescription()
    form = PrescriptionForm()
    if form.validate_on_submit():
        if request.method == 'POST' and Doctor.isAuthenticated and Doctor.isActive:
            prescription = Prescription(patientFirst=form.patientFirst.data,
                                        patientLast=form.patientLast.data,
                                        medication=form.medication.data,
                                        strength=form.strength.data,
                                        quantity=form.quantity.data,
                                        isSent=True,
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
    prescriptions = db.session.query(Prescription).order_by(Prescription.patientFirst).all()
    return render_template('prescriptionList.html', prescriptions=prescriptions)


@app.route('/medicalRecord/<record>')
def show_medical_record(record):
    print('Medical Record  %s' % record)
    return render_template('recordList.html')


if __name__ == "__main__":
    app.run(debug=True)
