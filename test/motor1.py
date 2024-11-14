import RPi.GPIO as GPIO
from time import sleep

# Pins definieren
in1 = 23  # Richtungspin 1
in2 = 24  # Richtungspin 2

# GPIO konfigurieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

# Software-PWM auf IN1
pwm = GPIO.PWM(in1, 1000)  # 1000 Hz
pwm.start(0)

try:
    while True:
        # Drehrichtung festlegen
        GPIO.output(in2, GPIO.LOW)  # Nur in eine Richtung fahren

        # Geschwindigkeit erhöhen
        for speed in range(0, 101, 5):  # Erhöhe die Geschwindigkeit in 5%-Schritten
            pwm.ChangeDutyCycle(speed)
            sleep(0.5)

        # Volle Geschwindigkeit für 2 Sekunden
        sleep(0.1)

        # Geschwindigkeit verringern
        for speed in range(100, -1, -5):  # Verringere die Geschwindigkeit in 5%-Schritten
            pwm.ChangeDutyCycle(speed)
            sleep(0.5)

        # Motor stoppen
        pwm.ChangeDutyCycle(0)
        sleep(2)

except KeyboardInterrupt:
    pass

# GPIO aufräumen
pwm.stop()
GPIO.cleanup()
