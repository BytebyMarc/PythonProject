import RPi.GPIO as GPIO
import time
import math

x = 2* math.pi


# GPIO-Modus auf BCM setzen
GPIO.setmode(GPIO.BCM)

# Sensor-Pin definieren
SENSOR_PIN = 36

# Sensor-Pin als Eingang festlegen
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        # Zustand des Sensors abfragen
        if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            print("Es ist hell")
        else:
            print("Es ist dunkel")

        # 1 Sekunde warten, um nicht zu häufig abzufragen
        time.sleep(1)

except KeyboardInterrupt:
    # Aufräumen bei Programmende
    print("Programm beendet")
finally:
    GPIO.cleanup()