import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


PIN_TRIGGER=3#number of PinInputOutput You have to change with your choice
PIN_ECHO=5
GPIO.setup(PIN_TRIGGER,GPIO.OUT)
GPIO.setup(PIN_ECHO,GPIO.IN)

while (True):
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    #distance = ((pulse_duration * 34300)/2)
    distance = round(((pulse_duration * 34300)/2), 2)
    
#This condition is simply Threshold 
    if (distance<=500):
    
        print("Distance:",distance,"cm")
        
    time.sleep(0.2)


GPIO.cleanup()