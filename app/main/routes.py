from flask import render_template, flash, request , Blueprint , jsonify
from flask_login import login_required , current_user
from app.models import Rig01 
import time
from random import sample

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    mes = Rig01.query.order_by(Rig01.Time_Stamp.desc()).all()
    return render_template('index.html', title='Home' , mesurments=mes)
