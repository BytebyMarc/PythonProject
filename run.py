import Enum

import Server
from Draw import *
from Motor import *
from FreeDrive import *
from MotorTest import *
from SensorTest import *
from SensorAutoDrive import *

draw = Draw()
motor = Motor()
freeDrive = FreeDrive()
motorTest = MotorTest()
sensorTest = SensorTest()
sensorAutoDrive = SensorAutoDrive()

run = 1
#client_socket = Server.serverStart()
draw.start()

while run == 1:
# speed = int(input("Geben sie eine Geschwindigkeit ein (1-10): "))
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         command = int(data.decode())
        command = int(input("Geben sie ein Menüpunkt ein:"))

        match command:
            case Enum.menu.freeDrive.value:
                freeDrive.start()
                draw.freeDrive()
            case Enum.menu.sensorAutoDrive.value:
                sensorAutoDrive.start()
                draw.sensorAutoDrive ()
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


#client_socket.close()
