import RPi.GPIO as GPIO
from time import sleep

# Pins definieren
in1 = 23  # Richtungspin 1
in2 = 24  # Richtungspin 2

in3 = 27  # Richtungspin 1
in4 = 22  # Richtungspin 2
# GPIO konfigurieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# Software-PWM auf IN1
pwm = GPIO.PWM(in1, 1000)  # 1000 Hz
pwm1 = GPIO.PWM(in3, 1000)  # 1000 Hz

pwm.start(0)
pwm1.start(0)
try:
    while True:
        # Drehrichtung festlegen
        GPIO.output(in2, GPIO.LOW)  # Nur in eine Richtung fahren
        GPIO.output(in4, GPIO.LOW)  # Nur in eine Richtung fahren
        # Geschwindigkeit erhöhen
        pwm.ChangeDutyCycle(50)
        pwm1.ChangeDutyCycle(50)
        sleep(0.1)

        # Volle Geschwindigkeit für 2 Sekunden
        sleep(0.1)

        # Geschwindigkeit verringern
        for speed in range(100, -1, -5):  # Verringere die Geschwindigkeit in 5%-Schritten
            pwm.ChangeDutyCycle(speed)
            pwm1.ChangeDutyCycle(speed)
            sleep(0.1)

        # Motor stoppen
        pwm.ChangeDutyCycle(0)
        pwm1.ChangeDutyCycle(0)
        sleep(2)

except KeyboardInterrupt:
    pass

# GPIO aufräumen
pwm.stop()
pwm1.stop()
GPIO.cleanup()
