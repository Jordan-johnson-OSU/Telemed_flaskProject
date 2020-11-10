import os
import flask
from flask import render_template
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
        Link('My Medical Records', 'medicalRecord/list'),
        Link('Create New', 'medicalRecord/new'),
        Link('Find Patient Medical Records', 'medicalRecord/search'),),
    Subgroup(
        'Payments',
        Link('My Payment Records', 'home'),
        Link('Make Payment', 'home'),),
    Subgroup(
        'Prescriptions',
        Link('My Prescriptions', 'home'),
        Link('Pending Prescription', 'home'),
        Link('New Prescription', 'home'),),
    ))

nav.init_app(app)

# Creating a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/telemedicine.db'
db = SQLAlchemy(app)

# we may want ot drop it and create it every time for testing
# db.drop_all()
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


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


@app.route('/medicalRecord/search')
def search_medical_records():
    return render_template('recordSearch.html')


@app.route('/medicalRecord/list')
def list_medical_records():
    return render_template('recordList.html')


@app.route('/medicalRecord/new')
def create_medical_record():
    return render_template('recordForm.html')


@app.route('/medicalRecord/<record>')
def show_medical_record(record):
    print('Medical Record  %d' % record)
    return render_template('recordForm.html')


app.run(debug=True)
