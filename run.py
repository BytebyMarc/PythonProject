import Enum
import Server
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from Draw import *
from Motor import *
from FreeDrive import *
from MotorTest import *
from SensorTest import *
from SensorAutoDrive import *
from Setup import *

GPIO.setmode(GPIO.BCM)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8) # LCD Initialising
# Motoren vorne Rechts
GPIO.setup(23, GPIO.OUT) # MotorDriver 1
GPIO.setup(24, GPIO.OUT) # MotorDriver 1
# Motoren vorne links
GPIO.setup(27, GPIO.OUT) # MotorDriver 2
GPIO.setup(22, GPIO.OUT) # MotorDriver 2
# Motoren Hinten Rechts
GPIO.setup(5, GPIO.OUT) # MotorDriver 3
GPIO.setup(6, GPIO.OUT) # MotorDriver 3
# Motoren hinten Links
GPIO.setup(13, GPIO.OUT) # MotorDriver 4
GPIO.setup(19, GPIO.OUT) # MotorDriver 4

GPIO.setup(17, GPIO.IN) # Sensor Helligkeit 0/1

GPIO.setup(16, GPIO.IN) # Ultraschall Sensor Trigger
GPIO.setup(20, GPIO.IN) # Ultraschall Sensor echo

GPIO.setup(12, GPIO.OUT) # RGB LED R
GPIO.setup(21, GPIO.OUT) # RGB LED G
GPIO.setup(18, GPIO.OUT) # RGB LED B

GPIO.setup(25, GPIO.OUT) # Big Sound modul
GPIO.setup(26, GPIO.OUT) # Big Sound modul

draw = Draw()
motor = Motor()
freeDrive = FreeDrive()
motorTest = MotorTest()
sensorTest = SensorTest()
sensorAutoDrive = SensorAutoDrive()
setup = Setup()

run = 1
client_socket = Server.serverStart()
draw.start()

while run == 1:
    Server.serverWhile(client_socket)
    command = int(input("Geben sie ein Menüpunkt ein:"))

    match command:
        case Enum.menu.freeDrive.value:
            freeDrive.start()
            draw.freeDrive()
        case Enum.menu.sensorAutoDrive.value:
            sensorAutoDrive.start()
            draw.sensorAutoDrive()
        case Enum.menu.sensorTest.value:
            sensorTest.start()
            draw.sensorTest()
        case Enum.menu.motorTest.value:
            motorTest.start()
            draw.motorTest()
        case Enum.menu.setup.value:
            setup.start()
            draw.setup()
        case Enum.menu.reboot.value:
            run = 0
            draw.reboot()
        case Enum.menu.shutdown.value:
            run = 0
            draw.stop()
        case _:
            print("Die Eingabe war ungültig")

# client_socket.close()
