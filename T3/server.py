import socket
import cv2
import pickle
import threading
import time

receive_ready = True

def receive_image(socket): # 卡在死循环出不来
    print('receiving image...')
    global receive_ready
    receive_ready = True
    data = b''
    while True:
        packet = socket.recv(4096)
        if not packet:
            break
        data += packet
    image = pickle.loads(data)
    receive_ready = False
    return image

def send_flag(client_socket):
    while True:
        time.sleep(0.1)
        if receive_ready:
            client_socket.send('RTS'.encode())
        else:
            client_socket.send('NRTS'.encode())
        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

server_socket.listen(5)

print('Waiting clients...')

client_socket, client_address = server_socket.accept()

print(f'{client_address} connected...')

sending_flag_thread = threading.Thread(target=send_flag, args=(client_socket,))
sending_flag_thread.start()


while True:
    img = receive_image(client_socket)
    print('image received!')
    cv2.imshow('Server', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

server_socket.close()
cv2.destroyAllWindows()


