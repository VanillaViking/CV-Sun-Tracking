import cv2
from ultralytics import YOLO
import RPi.GPIO as GPIO
import time
 
# Pin configuration

servo_pin = 16  # GPIO16 (pin 36 on RPi)
 
# PWM properties

pwm_freq = 50  # 50Hz for servos (20ms period)
 
# Setup

GPIO.setmode(GPIO.BCM)  # BCM pin numbering

GPIO.setup(servo_pin, GPIO.OUT)
 
# Set PWM on the pin with frequency

pwm = GPIO.PWM(servo_pin, pwm_freq)

pwm.start(0)  # Start PWM with 0% duty cycle
 

model = YOLO("best.pt")
cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    results = model(image)
    annotated_frame = results[0].plot()

    #cv2.imshow("Camera", image)
    try:
        print(results[0].boxes.xywh[0][1])
        duty_cycle = int((results[0].boxes.xywh[0][1] / 480) * 12)
        pwm.ChangeDutyCycle(duty_cycle)
    except:
        print("no detect")

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
