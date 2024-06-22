PATH = "/home/karlo/Documents/Charon/"
import ssl
import socket

def recive_file(secure_socket):
    try:
        with open(PATH+'received_file', 'wb') as f:
            while True:
                data = secure_socket.recv(4096)
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

    try:
        with open(filename, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                secure_socket.sendall(data)
        print('File sent successfully.')
    finally:
        secure_socket.close()