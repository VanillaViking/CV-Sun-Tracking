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
 
try:

    while True:

        # Ask for duty cycle input

        duty_cycle = input("Please enter your duty cycle (0-100): ")
 
        try:

            # Convert the input to integer

            duty_cycle = int(duty_cycle)
 
            # Limit the duty cycle to the valid range (0-100%)

            if 0 <= duty_cycle <= 100:

                pwm.ChangeDutyCycle(duty_cycle)

                print(f"Duty Cycle set to: {duty_cycle}%")

            else:

                print("Invalid value. Please enter a duty cycle between 0 and 100.")

        except ValueError:

            print("Invalid input. Please enter a numeric value.")

        time.sleep(0.01)
 
except KeyboardInterrupt:

    pass
 
finally:

    pwm.stop()

    GPIO.cleanup()
