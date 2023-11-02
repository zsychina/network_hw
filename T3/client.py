import socket
import cv2
import pickle
import threading

transmit_ready = False

def get_flag():
    global transmit_ready
    while True:
        data = client_socket.recv(1024)
        flag = data.decode()
        print(flag)
        if flag == 'RTS':
            transmit_ready = True
        elif flag == 'NRTS':
            transmit_ready = False
        else:
            print('Unknown flag')
        
def send_image(socket, img):
    img_serialized = pickle.dumps(img)
    socket.sendall(img_serialized)
    print('image sent...')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
client_socket.connect(server_address)

print('Server connected...')

getting_flag_thread = threading.Thread(target=get_flag)
getting_flag_thread.start()

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640, 480))
    
    print(transmit_ready)
    
    if transmit_ready:
        send_image(client_socket, img)
    
    # cv2.imshow('Client', img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break


client_socket.close()
cap.release()
    
    
