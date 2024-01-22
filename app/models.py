from app import db
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


########### USER MODEL ##############
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(12), nullable=False)

    def get_id(self): return self


######## TEAM MODEL ###########
class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(20), unique=True, nullable=False)
    team_mascota = db.Column(db.String)
    practices = db.relationship("Practice", backref="practice", lazy=True)


######## PRACTICE MODEL #######
class Practice(db.Model):
    practice_id = db.Column(db.Integer, primary_key=True)
    practice_lenght = db.Column(db.Integer)
    practice_date = db.Column(db.DateTime)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
