from flask import current_app , render_template, flash, request , Blueprint , jsonify ,send_from_directory
from flask_login import login_required , current_user
from app.models import Measurement 
import time
from random import sample

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    # current_app.logger.info('index')
    # mes = Measurement.query.order_by(Measurement.Time_Stamp.desc()).all()
    # return render_template('index.html', title='Home' , mesurments=mes)
    return render_template('index.html', title='Home' )

@main.route("/images/<image_name>")
def get_image(image_name):

    try:
        return send_from_directory("static/images", filename=image_name, as_attachment=True)
    except FileNotFoundError:
        print('Image Not found')

@main.route('/iot')
@login_required
def iot():
    return render_template('iot.html', title='iot' )