# importing the requests library 
import requests 
import time
# defining the api-endpoint  
URL = "http://127.0.0.1:5000/add"
  
# data to be sent to api 
PARAMS = {
        'TimeStamp':time.time(),
        'Temp1':'24.00', 
        'Temp2':'24.00', 
        'TAmbiant':'23.00', 
        'Humidity':'35'} 
  
# sending post request and saving response as response object 
r = requests.post(url = URL, data = PARAMS)

print("The response is %s"%r)

# extracting response text  
pastebin_url = r.text 

print("The Response Body is:%s"%pastebin_url) 