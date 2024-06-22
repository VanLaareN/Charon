import socket
import ssl

def send_file(server_ip, server_port, file_path, buffer_size=4096, certfile='server.crt'):
    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(certfile)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    with context.wrap_socket(client_socket, server_hostname=server_ip) as secure_socket:
        # Connect to the server
        secure_socket.connect((server_ip, server_port))
        print(f"[+] Connected to {server_ip}:{server_port}")

        # Send the file data
        with open(file_path, 'rb') as file:
            while True:
                bytes_read = file.read(buffer_size)
                if not bytes_read:
                    # File transmission is done
                    break
                secure_socket.sendall(bytes_read)
        print("[+] File sent successfully.")

        # Close the secure socket
        secure_socket.close()

# Usage
send_file(server_ip='127.0.0.1', server_port=5001, file_path='path_to_your_file')
