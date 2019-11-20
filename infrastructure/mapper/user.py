from domain.user import User as UserDomain
from infrastructure import db


class User(db.Model, UserDomain):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    # pumches = db.relationship('Punch', backred='punches')
