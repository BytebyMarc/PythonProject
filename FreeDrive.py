import keyboard
from time import sleep
import RPi.GPIO as GPIO

class FreeDrive:
    def __init__(self):
        speed = 0
        test = 2

    def start(self):
        speed = 0
        pwm22 = GPIO.PWM(22, 1000)  # 1000 Hz
        pwm23 = GPIO.PWM(23, 1000)  # 1000 Hz
        pwm24 = GPIO.PWM(24, 1000)  # 1000 Hz
        pwm27 = GPIO.PWM(27, 1000)  # 1000 Hz

        pwm22.start(0)
        pwm23.start(0)
        pwm24.start(0)
        pwm27.start(0)

        while True:

            match keyboard.read_key():
                case "nach-oben":
                    print("Oben")
                    pwm24.ChangeDutyCycle(0)
                    pwm22.ChangeDutyCycle(0)
                    #Motoren vorne rechts
                    pwm23.ChangeDutyCycle(speed)
                    # Motoren vorne links
                    pwm27.ChangeDutyCycle(speed)

                case "nach-unten":
                    pwm23.ChangeDutyCycle(0)
                    pwm27.ChangeDutyCycle(0)
                    #Motoren vorne rechts
                    pwm24.ChangeDutyCycle(speed)
                    # Motoren vorne links
                    pwm22.ChangeDutyCycle(speed)

                case "nach-links":
                    print("Links")

                case "nach-rechts":
                    print("Rechts")

                case "+":
                        speed = speed + 5
                        print(speed)
                        if speed <= 100:
                            speed = 100

                case "-":
                    speed = speed - 5
                    print(speed)
                    if speed <= 0:
                        speed = 0
                case "esc":
                    GPIO.output(22, GPIO.LOW)
                    GPIO.output(23, GPIO.LOW)
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)

    sleep(0.1)


freeDrive = FreeDrive()
freeDrive.start()
