from domain.punch import Punch as PunchDomain
from infrastructure import db


class Punch(db.Model, PunchDomain):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
