# from datetime import datetime
from flask import current_app
from app import db , login
from flask_login import UserMixin   #for user logins
from werkzeug.security import generate_password_hash, check_password_hash
import time


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Rig01(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dbTime_Stamp = db.Column(db.Float() , default=time.time)
    Time_Stamp = db.Column(db.Float() , default=time.time, index=True)
    Temp1 = db.Column(db.Float(), unique=False , nullable=True)
    Temp2 = db.Column(db.Float(), unique=False , nullable=True)
    Tambiant =  db.Column(db.Float(), unique=False , nullable=True)
    Humidity  =  db.Column(db.Float(), unique=False , nullable=True)
    

    def __repr__(self):
        return f"Mesurment('{self.dbTime_Stamp}','{self.Time_Stamp}', {self.Temp1} ,{self.Temp2} ,{self.Tambiant}, {self.Humidity})"

# db.create_all()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))