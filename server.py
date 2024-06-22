import socket
import ssl

def receive_file(server_ip, server_port, buffer_size=4096, save_path='received_file', certfile='server.crt', keyfile='server.key'):
    # Create an SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to the server IP and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"[*] Listening on {server_ip}:{server_port}")

    # Accept a connection and wrap the socket with SSL
    with context.wrap_socket(server_socket, server_side=True) as secure_socket:
        client_socket, addr = secure_socket.accept()
        print(f"[+] Connection from {addr} established.")

        # Receive the file data
        with open(save_path, 'wb') as file:
            while True:
                bytes_read = client_socket.recv(buffer_size)
                if not bytes_read:
                    # File transmission is done
                    break
                file.write(bytes_read)
        print("[+] File received successfully.")

        # Close the client socket
        client_socket.close()

    # Close the server socket
    server_socket.close()

# Usage
receive_file(server_ip='0.0.0.0', server_port=5001)
