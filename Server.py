import socket


def serverStart():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("Warte auf Verbindung...")
    client_socket, client_address = server_socket.accept()
    return client_socket


def serverWhile(client_socket, ):

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        command = int(data.decode())
    return command

#
#
# def start_server(command):
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('0.0.0.0', 12345))
#     server_socket.listen(1)
#     print("Warte auf Verbindung...")
#
#     client_socket, client_address = server_socket.accept()
#     print(f"Verbindung von {client_address} hergestellt.")
#
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         command = int(data.decode())
#         # Verarbeite den Integer-Befehl
#         print(f"Befehl empfangen: {command}")
#         # Hier kannst du den Befehl an die entsprechende Funktion weiterleiten
#
#     client_socket.close()
