import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)


server_socket.listen(5)
print('Waiting clients...')


client_sockets = []

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if data:
            print(f'{client_address}: {data.decode()}')
            # broadcast
            for client in client_sockets:
                client.sendall(data)
        else:
            client_socket.close()
            client_sockets.remove(client_socket)
            print(f'{client_address} disconnected, current user: {len(client_sockets)}')
            break

while True:
    client_socket, client_address = server_socket.accept()
    client_sockets.append(client_socket)
    
    print(f'{client_address} has connected, current user: {len(client_sockets)}')

    # create thread for each connected client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
    
server_socket.close()
