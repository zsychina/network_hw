import socket

client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

host = socket.gethostname()

port = 12345

client_socket.connect((host, port))

print('Client connected to server!')

while True:
    data = input()
    
    client_socket.send(data.encode('utf-8'))
    
client_socket.close()

