import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)  # MotorDriver 1
GPIO.setup(27, GPIO.OUT)  # MotorDriver 1

pwm = GPIO.PWM(27, 1000)  # 1000 Hz
pwm1 = GPIO.PWM(22, 1000) # 1000 Hz
pwm.start(0)
pwm1.start(0)
print("\n")
print("Motor test")
print("\n")
i = 1
# vorwährts
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

while i < 30:

    pwm.ChangeDutyCycle(25)
    sleep(0.1)
    i += 1

GPIO.output(27, GPIO.LOW)
print("forward")
x = 'z'
