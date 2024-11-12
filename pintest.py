import RPi.GPIO as GPIO
import time
000000000000000000000000000000000000000000000000000000000000000000000000000000000
# GPIO-Modus auf BCM setzen
GPIO.setmode(GPIO.BCM)

# Liste von Pins, die du testen möchtest (z. B. GPIO 17, 27, 22, 5)
test_pins = [3,5,7,11,13,15,16,18,22,270,,31,36,37]

# Pins als Ausgang festlegen und testen
for pin in test_pins:
    GPIO.setup(pin, GPIO.OUT)
    print(f"Pin {pin} wird auf HIGH gesetzt.")
    GPIO.output(pin, GPIO.HIGH)
  #  time.sleep(1)  # 1 Sekunde warten
   # GPIO.output(pin, GPIO.LOW)
  #  print(f"Pin {pin} wird auf LOW gesetzt.")
  #  time.sleep(1)  # 1 Sekunde warten

# Pins als Eingang festlegen und testen
for pin in test_pins:
    GPIO.setup(pin, GPIO.IN)
    input_state = GPIO.input(pin)
    if GPIO.input(pin) == GPIO.HIGH:
        print("Es ist hell")
    print(f"Pin {pin} ist auf {input_state} (HIGH oder LOW).")


# Aufräumen
GPIO.cleanup()