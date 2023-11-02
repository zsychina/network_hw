import socket
import cv2
import pickle

def receive_image(socket):
    flame_finished = False
    socket.send(str(flame_finished))
    data = b''
    while True:
        packet = socket.recv(4096)
        if not packet:
            break
        data += packet
    try:
        image = pickle.loads(data)
        flame_finished = True
        socket.send(str(flame_finished))
        return image
    except pickle.UnpicklingError as e:
        print(e)
        return None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

server_socket.bind((host, port))
server_socket.listen(5)
print(f'host: {host}, port: {port}')

client_socket, client_addr = server_socket.accept()
print(f'{client_addr} connected!')


while True:
    try:
        image = receive_image(client_socket)
        if image is not None:
            cv2.imshow('Server', image)
    except socket.error as e:
        print(f"Socket error: {e}")
        break
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


server_socket.close()
cv2.destroyAllWindows()

