from flask import render_template, redirect, url_for, request , Blueprint , jsonify
from flask_login import login_required 
from app.models import Measurement , Metadata
from flask import current_app
from app import db
from datetime import datetime
import time
import requests

function = Blueprint('function', __name__)
# route for adding a measurment to the data base
@function.route('/add', methods=['GET'])
def add():
    if request.method == 'GET':
        data = request.values.to_dict()     # get the measurments into a dicionary
        try:
            WEATHER_API_URL= Metadata.query.order_by(Metadata.API_URL).first().API_URL
            api_data = requests.get(WEATHER_API_URL , timeout=10).json()    # weather API
            mesur = Measurement (
                    RigId=data['RigId'],
                    Time_Stamp=(data['TimeStamp']), 
                    Temp1=float(data['Temp1']), 
                    Temp2=float(data['Temp2']), 
                    Tambiant=float(data['TAmbiant']), 
                    Humidity=float(data['Humidity']),
                    API_Temp=api_data['main']['temp'] - 273.15 ,
                    API_Humidity=api_data['main']['humidity'] ,
                    API_Pressure=api_data['main']['pressure'] ,
                    API_WindSpeed=api_data['wind']['speed'] ,
                    API_WindDeg=api_data['wind']['deg'] ,
                    API_Weather=api_data['weather'][0]['main']
                    )

            db.session.add(mesur)       # add the measur to the data base
            db.session.commit()
        except:
            # API request failled
            mesur = Measurement (
                    Time_Stamp=(data['TimeStamp']), 
                    Temp1=float(data['Temp1']), 
                    Temp2=float(data['Temp2']), 
                    Tambiant=float(data['TAmbiant']), 
                    Humidity=float(data['Humidity'])
                    )
            db.session.add(mesur)
            db.session.commit()
        return "GET"
    return 200

# route for droping the measurments table
@function.route('/delete')
@login_required
def delete():
    try:
        num_rows_deleted = db.session.query(Measurement).delete()
        print(num_rows_deleted)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('main.index'))

# route for getting the data out of the data base 
@function.route('/data')
# @login_required
def data():
    qresponse = Measurement.query.order_by(Measurement.Time_Stamp.desc()).all()
    xAxe = []
    t1vec = [] 
    t2vec = []
    tambvec  = []
    humidity = []
    for i in qresponse:
        xAxe.append(datetime.fromtimestamp(i.Time_Stamp).strftime("%Y-%m-%d %H:%M:%S"))
        t1vec.append(i.Temp1)
        t2vec.append(i.Temp2)
        tambvec.append(i.Tambiant)
        humidity.append(i.Humidity)
    data = jsonify({'time':xAxe , 'Temp1':t1vec , 'Temp2':t2vec , 'Tambiant':tambvec , 'Humidity':humidity})
    return data

# route for getting the data out of the data base 
@function.route('/api_data')
# @login_required
def api_data():
    WEATHER_API_URL = Metadata.query.order_by(Metadata.API_URL).first().API_URL
    json_data =jsonify(requests.get(WEATHER_API_URL).json())
    return json_data
