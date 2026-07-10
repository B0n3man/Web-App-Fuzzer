#from flask import logging
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

def handle_client(client_socket):

    print("Recieved request\n")
    request = b''
    client_socket.setblocking(False)

    while True:
        try:
            data = client_socket.recv(1024)
            request += data
        except:
            break

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr} has been established...")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

