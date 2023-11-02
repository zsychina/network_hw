import socket
import cv2
import pickle

def send_image(socket, img):
    img_serialized = pickle.dumps(img)
    socket.sendall(img_serialized)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client_socket.connect((host, port))

print('Client connected to server!')

cap = cv2.VideoCapture(0)

transmit_ready = True

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640, 480))
    
    if transmit_ready:
        send_image(client_socket, img)
        
    transmit_ready = client_socket.recv(1024).decode()
    print(transmit_ready)
    
    cv2.imshow('Client', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()

cap.release()
cv2.destroyAllWindows()
