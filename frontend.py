import flask

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

from .forms import LoginForm
from .nav import nav

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(
    View('Flask-Bootstrap', '.index'),
    View('Home', '.index'),
    View('Forms Example', '.example_form'),
    View('Debug-Info', 'debug.debug_root'),
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Separator(),
        Text('Bootstrap'),
        Link('Getting started', 'http://getbootstrap.com/getting-started/'),
        Link('CSS', 'http://getbootstrap.com/css/'),
        Link('Components', 'http://getbootstrap.com/components/'),
        Link('Javascript', 'http://getbootstrap.com/javascript/'),
        Link('Customize', 'http://getbootstrap.com/customize/'), ),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), ))


#
# @login_manager.user_loader
# def load_user(user_id):
#    return User.get(user_id)


@frontend.route('/', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        # login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')

        return flask.redirect(next or flask.url_for('home'))
    return flask.render_template('index.html', form=form)


@frontend.route("/logout")
# @login_required
def logout():
    # do logout
    return render_template('index.html')


@frontend.route('/home')
def home():
    return render_template('home.html')


@frontend.route('/medicalRecord/list')
def list_medical_records():
    return render_template('recordList.html')


@frontend.route('/medicalRecord/new')
def create_medical_record():
    return 'Medical Record - new'
    # return render_template('recordForm.html')


@frontend.route('/medicalRecord/<int:id>')
def show_medical_record(id):
    return 'Medical Record  %d' % id
    # return render_template('recordForm.html')
