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

