import RPi.GPIO as GPIO
import time
import json
import requests # importing the requests library
from json_tricks import dumps


API_ENDPOINT="https://geoffish.herokuapp.com/api/post_distance/"
print ("distance measurement in progress")
while True:
    GPIO.setmode(GPIO.BCM)

    TRIG=23
    ECHO=24



    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG,False)

   


    time.sleep(3)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=int (round(distance))
    #data.append({" distance ":distance})
    #js_data=dumps(data)
    print(distance)
    time.sleep(5)
    r=requests.post(url=API_ENDPOINT, data={'data':distance})
    print (r)

    GPIO.cleanup()

    
    




           
