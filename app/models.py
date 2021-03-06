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

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True , index=True)
    RigId = db.Column(db.String(16) , unique=False , nullable=False)
    dbTime_Stamp = db.Column(db.Float() , default=time.time)
    Time_Stamp = db.Column(db.Float() , default=time.time, nullable=False , index=True)
    Temp1 = db.Column(db.Float(), unique=False , nullable=True)
    Temp2 = db.Column(db.Float(), unique=False , nullable=True)
    Tambiant =  db.Column(db.Float(), unique=False , nullable=True)
    Humidity  =  db.Column(db.Float(), unique=False , nullable=True)
    API_Temp = db.Column(db.Float(), unique=False , nullable=True , default=None)
    API_Humidity = db.Column(db.Integer(), unique=False , nullable=True ,default=None)
    API_Pressure = db.Column(db.Float(), unique=False , nullable=True , default=None)
    API_WindSpeed = db.Column(db.Float(), unique=False , nullable=True , default=None)
    API_WindDeg = db.Column(db.Float(), unique=False , nullable=True , default=None)
    API_Weather = db.Column(db.String(32), unique=False , nullable=True , default=None)

    def __repr__(self):
        return f"Mesurment({self.dbTime_Stamp},{self.Time_Stamp}, {self.Temp1} ,{self.Temp2} ,{self.Tambiant}, {self.Humidity} , \
                            {self.API_Temp},{self.API_Humidity}, {self.API_Pressure} ,{self.API_WindSpeed} ,{self.API_WindDeg}, {self.API_Weather})"


class Metadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    RigId = db.Column(db.String(16) , unique=True , nullable=False)
    API_URL = db.Column(db.String(128) , unique=False , nullable=False)
    interval = db.Column(db.Integer, unique=False , nullable=False , default=60)
    def __repr__(self):
        return f"Metadata({self.API_URL})"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))