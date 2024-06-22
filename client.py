from socket_methods import *

LOCALHOST = 'localhost'
PORT = 12345
FILE = PATH+'example.txt'

if __name__ == "__main__":
    send_file(LOCALHOST, PORT, FILE)
