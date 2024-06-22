def receive_file(client_socket, buffer_size=4096, save_path="C:\\Users\\karlo\\Documents\\Python Shit\\sync files\\recived_file.txt"):
    # Receive the file data
    with open(save_path, 'wb') as file:
        while True:
            bytes_read = client_socket.recv(buffer_size)
            if not bytes_read:
                # File transmission is done
                break
            file.write(bytes_read)
    print("[+] File received successfully.")

    # Close the sockets
    client_socket.close()


def send_file(client_socket, file_path, buffer_size=4096):
    # Send the file data
    with open(file_path, 'rb') as file:
        while True:
            bytes_read = file.read(buffer_size)
            if not bytes_read:
                # File transmission is done
                break
            client_socket.sendall(bytes_read)
    print("[+] File sent successfully.")