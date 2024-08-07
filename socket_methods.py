import ssl
import socket

PATH = "/home/karlo/Documents/Charon/"
BUFFER = 4096

def receive_file(secure_socket):
    filename = receive_text(secure_socket)
    print(f'Filename received: {filename}')
    try:
        with open(PATH + "server/" + filename, 'wb') as f:
            while True:
                data = secure_socket.recv(BUFFER)
                if not data:
                    break
                f.write(data)
        print('File received successfully.')
    finally:
        secure_socket.close()

def send_file(server_host, server_port, filename):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_socket = context.wrap_socket(raw_socket, server_hostname=server_host)

    secure_socket.connect((server_host, server_port))
    print(f'Connected to {server_host}:{server_port}')

    send_text(secure_socket, filename.split("/")[-1])

    try:
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER)
                if not data:
                    break
                secure_socket.sendall(data)
        print('File sent successfully.')
    finally:
        secure_socket.close()

def receive_text(secure_socket):
    data = secure_socket.recv(BUFFER).decode('utf-8')
    return data

def send_text(secure_socket, text):
    try:
        secure_socket.sendall(text.encode('utf-8'))
        print(f'Text sent successfully: {text}')
    except Exception as e:
        print(f'Failed to send text: {e}')
