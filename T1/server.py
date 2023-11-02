import socket

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

host = socket.gethostname()

port = 12345

print(f'host: {host}, port: {port}')

server_socket.bind((host, port))

server_socket.listen(5)

client_socket, client_addr = server_socket.accept()

while True:
    data = client_socket.recv(1024)
    
    print(data.decode('utf-8'))
    
server_socket.close()
    
    
    



