import socket


def send_commands():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('thecar.local', 12345))  # Hier den Hostnamen verwenden

    try:
        while True:
            command = int(input('Enter command: '))  # Eingabe als Integer umwandeln
            client_socket.send(str(command).encode())  # Integer zu String und dann zu Bytes kodieren
    except KeyboardInterrupt:
        print("Verbindung wird geschlossen...")
    finally:
        client_socket.close()


send_commands()