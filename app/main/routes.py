from flask import render_template, flash, request , Blueprint , jsonify
from flask_login import login_required , current_user
from app.models import Rig01 
import time
from random import sample

# from app import db

# import decimal, datetime

# def alchemyencoder(obj):
#     """JSON encoder function for SQLAlchemy special classes."""
#     if isinstance(obj, datetime.date):
#         return obj.isoformat()
#     elif isinstance(obj, decimal.Decimal):
#         return float(obj)

# def example():
#     res = Rig01.select().order_by(Rig01.Time_Stamp.desc()).limit(5)
#     print(res)
#     # use special handler for dates and decimals
#     return json.dumps([dict(r) for r in res], default=alchemyencoder)


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    # page = request.args.get('page',1,type=int)
    # print(page)
    # return "Hello, World!"
    # mes = Rig01.query.all()
    # mes = Rig01.query.paginate(page=page , per_page=20)
    # mes = Rig01.query.order_by(Rig01.Time_Stamp.desc()).paginate(page=page , per_page=20)
    mes = Rig01.query.order_by(Rig01.Time_Stamp.desc()).all()
    # print(mes)
    # mes = {
    #     'TimeStamp':time.time() ,
    #     'Temp1':24.00, 
    #     'Temp2':24.00, 
    #     'TAmbiant':23.00, 
    #     'Humidity':35} 

    # for i in range(1,4320):
    #     if(len-i):
    #         point = Rig01.query.get(len-i)
    #         xAxe.append(datetime.fromtimestamp(point.Time_Stamp).strftime("%Y-%d-%m %H:%M:%S"))
    #         t1vec.append(point.Temp1)
    #         t2vec.append(point.Temp2)
    #         tambvec.append(point.TAmbiant)
    #         humidity.append(point.Humidity)
    #     else:
    #         break
    return render_template('index.html', title='Home' , mesurments=mes)
