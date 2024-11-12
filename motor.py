import RPi.GPIO as GPIO
import time

# GPIO-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# Definiere die GPIO-Pins für Motor A
IN1 = 17
IN2 = 18

# Definiere die GPIO-Pins für Motor B
IN3 = 22
IN4 = 23

# Definiere die PWM-Pins für die Motorsteuerung (optional)
ENA = 25  # Motor A PWM
ENB = 24  # Motor B PWM

# Setup der GPIO-Pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# PWM-Objekte erstellen (optional, für Geschwindigkeit)
pwmA = GPIO.PWM(ENA, 1000)  # 1000 Hz PWM für Motor A
pwmB = GPIO.PWM(ENB, 1000)  # 1000 Hz PWM für Motor B

# PWM starten
pwmA.start(0)  # Start mit 0% Geschwindigkeit
pwmB.start(0)  # Start mit 0% Geschwindigkeit

# Motor in eine Richtung drehen (z. B. Motor A im Uhrzeigersinn und Motor B gegen den Uhrzeigersinn)
def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Vorwärts fahren
forward()

# Motorgeschwindigkeit mit PWM steuern (0-100%)
pwmA.ChangeDutyCycle(75)  # 75% Geschwindigkeit für Motor A
pwmB.ChangeDutyCycle(75)  # 75% Geschwindigkeit für Motor B

# Warte für 5 Sekunden
time.sleep(5)

# Stoppe die Motoren
stop()

# Aufräumen
GPIO.cleanup()