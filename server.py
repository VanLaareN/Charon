PATH = "/home/karlo/Documents/Charon/"


import socket
import ssl

def create_server(host, port, certfile, keyfile):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile, keyfile)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f'Server listening on {host}:{port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')
        secure_socket = context.wrap_socket(client_socket, server_side=True)
        
        try:
            with open(PATH+'received_file.txt', 'wb') as f:
                while True:
                    data = secure_socket.recv(4096)
                    if not data:
                        break
                    f.write(data)
            print('File received successfully.')
        finally:
            secure_socket.close()

if __name__ == "__main__":
    create_server('localhost', 12345, PATH+'cert.pem', PATH+'key.pem')
