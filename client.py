from socket_methods import PATH
from socket_methods import send_file

if __name__ == "__main__":
    send_file('localhost', 12345, PATH+'example.txt')


