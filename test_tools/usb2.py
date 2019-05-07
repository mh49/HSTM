import time
import serial
import serial.tools.list_ports
import ast
import warnings
import requests
# from datetime import datetime

URL = "http://127.0.0.1:5000/add"  # main server 

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]

if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    print('Multiple Arduinos found - using the first')

arduino = serial.Serial(arduino_ports[0])

arduino.flushInput()

#print(arduino.__sizeof__())
i=5
while (i):
    if (arduino.inWaiting()>=16):
        # print(arduino.inWaiting())
        results = str(arduino.readline())
        
        # print(results)
        results = results.replace("b\"",'')
        results = results[:-5]
        # print(results)

        results = eval(results)
        # print(type(results))
        results['TimeStamp']=time.time() 

        r = requests.get(url = URL , data=results) 
        print(r)
        time.sleep(58)
        # i-=1

        # named_tuple = time.localtime(Time_Stampe) # get struct_time
        # time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        # Date = time_string.split(',')[0]
        # Time = time_string.split(', ')[1]
        # #print(results)
        # Data = ast.literal_eval(results)
        # # print(Data)
        # print(str(Time_Stampe) +" " + Date +" " + Time + " " + results)
        # text = str(Time_Stampe) + ";" +Date + ";" + Time + ";" + Data['Ambiant'] +';'+ Data['Temp 1'] +';'+ Data['Temp 2'] +';'+ Data['Humidity'] +';'+"\n"
    # time.sleep(1)