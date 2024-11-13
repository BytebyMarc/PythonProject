import App
import socket
from Draw import *
from Motor import *

draw = Draw()
motor = Motor()

run = 1
# ---------------------------------------------------------
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)
print("Warte auf Verbindung...")

client_socket, client_address = server_socket.accept()
print(f"Verbindung von {client_address} hergestellt.")
# -----------------------------------------------------------

draw.start()
while run == 1:

# speed = int(input("Geben sie eine Geschwindigkeit ein (1-10): "))
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        command = int(data.decode())

        match command:
            case App.menu.straightAhead.value:
                motor.straightAhead()
                draw.straightAhead()
            case App.menu.returns.value:
                motor.returns()
                draw.returns()
            case App.menu.left.value:
                motor.left()
                draw.left()
            case App.menu.right.value:
                motor.right()
                draw.right()
            case App.menu.stop.value:
                motor.stop()
            case App.menu.quit.value:
                run = 0
                draw.stop()
            case _:
                print("Die Eingabe war ungültig")


client_socket.close()
