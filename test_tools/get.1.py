
# importing the requests library 
import requests 
import time

# URL to send the data to
URL = "http://127.0.0.1:5000/add"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {
        'TimeStamp':time.time() ,
        'Temp1':24.00, 
        'Temp2':24.00, 
        'TAmbiant':23.00, 
        'Humidity':35} 
i=31104000
while(i):
        # print("params: %s"%PARAMS)
# sending get request and saving the response as response object 
        r = requests.get(url = URL , data=PARAMS) 
        print(i)
        i-=1
# print("The Response Body is:%s"%r.text) 
