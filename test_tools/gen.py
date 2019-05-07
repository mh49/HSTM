import time
from app import db
from app.main.models import Rig01

t1 = time.time()
q = Rig01.query.all()
t2 = time.time()
print(t2 - t1)

# data = {
#         'TimeStamp':time.time() ,
#         'Temp1':24.00, 
#         'Temp2':24.00, 
#         'TAmbiant':23.00, 
#         'Humidity':35} 

# i=7776000    #3 mois            #31104000 #1an
# while(i):
#     mesur = Rig01 (
#                         Time_Stamp=time.time(), 
#                         Temp1=float(data['Temp1']), 
#                         Temp2=float(data['Temp2']), 
#                         Tambiant=float(data['TAmbiant']), 
#                         Humidity=float(data['Humidity']) 
#                         )

#     db.session.add(mesur)
#     db.session.commit()
#     i-=1
#     print(i)