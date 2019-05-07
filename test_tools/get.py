
# importing the requests library 
import requests 
import time
# from datetime import datetime

# URL to send the data to
URL = "http://127.0.0.1:5000/add"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {
        'TimeStamp':time.time() ,
        'Temp1':24.00, 
        'Temp2':24.00, 
        'TAmbiant':23.00, 
        'Humidity':35} 

print("params: %s"%PARAMS)
# sending get request and saving the response as response object 
r = requests.get(url = URL , data=PARAMS) 
print(r)
# print("The Response Body is:%s"%r.text) 
