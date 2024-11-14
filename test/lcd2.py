from RPLCD.i2c import CharLCD
import time

try:
    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
    lcd.clear()
    lcd.write_string('Hello, World!')
    print("Nachricht erfolgreich gesendet.")
    time.sleep(5)
    lcd.clear()
except Exception as e:
    print("Fehler:", e)
