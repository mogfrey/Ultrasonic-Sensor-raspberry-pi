import serial
import RPi.GPIO as GPIO
import os, time
from time import sleep 


GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings
OutputPins = [5]
# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=5)

    

    
def sms_warning():
    time.sleep(1)
    port.write(('AT'+'\r\n').encode())
    time.sleep(1)
    port.write(('ATE0'+'\r\n').encode())      # Disable the Echo
    time.sleep(1)
    port.write(('AT+CMGF=1'+'\r\n').encode())  # Select Message format as Text mode 
    time.sleep(1)
    port.write(('AT+CNMI=2,1,0,0,0'+'\r\n').encode())   # New SMS Message Indications
    time.sleep(1)
    # Sending a message to a particular Number
         
    port.write(('AT+CMGS="0726309019"'+'\r\n').encode())
    #rcv = port.read(10)
    #print (rcv)
    
    time.sleep(1)
    
def call_warning():
    port.write(('ATD0726309019;'+'\r').encode())
    

   

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
    distance=round(distance,2)
    print("checking level threshold")
    
    if (distance)<=5:
        print("WARNING !! water level too low!!")
        
        call_warning()
        sms_warning()

           
        port.write(('WARNING !! water level too low. Refill in progress!!'+'\r').encode())  # Message
        time.sleep(1)
        port.write(("\x1A").encode()) # Enable to send SMS
        time.sleep(1)

        print("Refill in progress..")

        for i in OutputPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
        sleep(5)
        for i in OutputPins:
            GPIO.output(i, True)
        sleep(5)
        


     
        
        
        time.sleep(120)
    
