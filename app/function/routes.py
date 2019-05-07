from flask import render_template, redirect, url_for, request , Blueprint , jsonify
from flask_login import login_required 
from app.models import Rig01
from flask import current_app
from app import db
from datetime import datetime
import time
import requests

WEATHER_API_URL='http://api.openweathermap.org/data/2.5/weather?id=2487134&APPID=046afe7166cc4ba51e9ef2026ce0e362'

function = Blueprint('function', __name__)

# route for adding a measurment to the data base
@function.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # print("POST Request:")
        # print("Req.url: %s"%request.url)
        # print("Req.args: %s"%request.args)
        # print("Req.form: %s"%request.form)
        # print("Req.values: %s"%request.values)

        data = request.values.to_dict()
        data['dbTimeStamp']=time.time()

        print("dbTimeStamp:%s \nTimeStamp:%s \nTemp1:%s \nTemp2:%s \nTAmbiant:%s \nHumidity:%s \n"%
                                                                        (
                                                                        data['dbTimeStamp'],
                                                                        data['TimeStamp'],
                                                                        data['Temp1'],
                                                                        data['Temp2'],
                                                                        data['TAmbiant'],
                                                                        data['Humidity']
                                                                        )
            )

        return "POST"

    else:
        # print the request
        # print("GET Request:")
        # print("Req.url: %s"%request.url)
        # print("Req.args: %s"%request.args)
        # print("Req.form: %s"%request.form)
        # print("Req.values: %s"%request.values)

        data = request.values.to_dict()
        data['dbTimeStamp']=time.time()

        # print("data:%s"%data)
        # print("type:%s"%type(data))

        # print("dbTimeStamp:%s \nTimeStamp:%s \nTemp1:%s \nTemp2:%s \nTAmbiant:%s \nHumidity:%s \n"%
        #                                                                         (
        #                                                                         data['dbTimeStamp'],
        #                                                                         data['TimeStamp'],
        #                                                                         data['Temp1'],
        #                                                                         data['Temp2'],
        #                                                                         data['TAmbiant'],
        #                                                                         data['Humidity']
        #                                                                         )
        #             )

        
        # api_data={}
        try:
            api_data = requests.get(WEATHER_API_URL , timeout=10).json()

            mesur = Rig01 (
                    # dbTime_Stamp=time.time(),
                    Time_Stamp=(data['TimeStamp']), 
                    Temp1=float(data['Temp1']), 
                    Temp2=float(data['Temp2']), 
                    Tambiant=float(data['TAmbiant']), 
                    Humidity=float(data['Humidity']),
                    Temp=api_data['main']['temp'] - 273.15 ,
                    API_Humidity=api_data['main']['humidity'] ,
                    Pressure=api_data['main']['pressure'] ,
                    WindSpeed=api_data['wind']['speed'] ,
                    WindDeg=api_data['wind']['deg'] ,
                    Weather=api_data['weather'][0]['main']
                    )

            db.session.add(mesur)
            db.session.commit()

        except:
            print("api exception")

            mesur = Rig01 (
                    # dbTime_Stamp=time.time(),
                    Time_Stamp=(data['TimeStamp']), 
                    Temp1=float(data['Temp1']), 
                    Temp2=float(data['Temp2']), 
                    Tambiant=float(data['TAmbiant']), 
                    Humidity=float(data['Humidity'])
                    )

            db.session.add(mesur)
            db.session.commit()
        # print(mesur.Time_Stamp)
        # print(db.session.query_property())

        # s= Rig01.query.all()
        # print(s)
        return "GET"
    return 200

# route for droping the measurments table
@function.route('/delete')
@login_required
def delete():
    try:
        num_rows_deleted = db.session.query(Rig01).delete()
        print(num_rows_deleted)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('main.index'))

# route for getting the data out of the data base 
@function.route('/data')
@login_required
def data():

    qresponse = Rig01.query.order_by(Rig01.Time_Stamp.desc()).limit(2592000).all()
    xAxe = []
    t1vec = [] 
    t2vec = []
    tambvec  = []
    humidity = []
    for i in qresponse:
        # print(datetime.fromtimestamp(i.Time_Stamp).strftime("%Y-%m-%d %H:%M:%S"))
        xAxe.append(datetime.fromtimestamp(i.Time_Stamp).strftime("%Y-%m-%d %H:%M:%S"))
        t1vec.append(i.Temp1)
        t2vec.append(i.Temp2)
        tambvec.append(i.Tambiant)
        humidity.append(i.Humidity)
    # print(xAxe)
    # print(t1vec)
    # print(t2vec)
    # print(tambvec)
    # print(humidity)
    data = jsonify({'time':xAxe , 'Temp1':t1vec , 'Temp2':t2vec , 'Tambiant':tambvec , 'Humidity':humidity})
    return data
