import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.15.183.54', 12345)

client_socket.connect(server_address)
print(f'Server {server_address} connected...')

def receive_message():
    while True:
        data = client_socket.recv(1024)
        if data:
            print(f'msg from server: {data.decode()}')


receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

while True:
    message = input()
    client_socket.sendall(message.encode())

client_socket.close()
    