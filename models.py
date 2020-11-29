from app import db

# See Flask-alchemy documentation : https://flask-sqlalchemy.palletsprojects.com/en/2.x/


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r >' % self.user_id

    def is_authenticated(self):
        return 1

    def is_active(self):
        return 1

    def is_anonymous(self):
        return 1

    def get_id(self):
        return self.user_id


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r %r>' % self.first_name % self.last_name


# TODO
# Create Doctor and Diagnosis model
# create relationships between all the models
class IndexTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s1 = db.Column(db.String(50), unique=True, nullable=False)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctorID = db.Column(db.String(50))
    isActive = True
    isAuthenticated = True
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    provider = db.Column(db.String(50))


class Allergy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientFirstName = db.Column(db.String(50))
    patientLastName = db.Column(db.String(50))
    allergyMedication = db.Column(db.String(50))
    allergyDescription = db.Column(db.String(500))
    # dateEntered = db.Column(db.Date())
    createdBy = db.Column(db.String(50))


class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    treatment = db.Column(db.String(50))


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientFirst = db.Column(db.String(50), nullable=False)
    patientLast = db.Column(db.String(50), nullable=False)
    medication = db.Column(db.String(50), nullable=False)
    strength = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    isSent = None
    directions = db.Column(db.String(80), nullable=False)


class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientFirst = db.Column(db.String(80), unique=True, nullable=False)
    patientLast = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    doctorID = db.Column(db.String(50), unique=True, nullable=False)
    drFirst = db.Column(db.String(50), unique=True, nullable=False)
    drLast = db.Column(db.String(50), unique=True, nullable=False)
    provider = db.Column(db.String(50), unique=True, nullable=False)
    disease = db.Column(db.String(50), unique=True, nullable=False)
    condition = db.Column(db.String(50), unique=True, nullable=False)
    treatment = db.Column(db.String(50), unique=True, nullable=False)
    medication = db.Column(db.String(50), unique=True, nullable=False)
    strength = db.Column(db.String(50), unique=True, nullable=False)
    directions = db.Column(db.String(80), unique=True, nullable=False)