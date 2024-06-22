from socket_methods import *
from observer import Watcher
import threading
from queue import Queue
import time 

LOCALHOST = 'localhost'
PORT = 12345
FILE = PATH + 'example.txt'

def wachter_thread(q):
    watcher = Watcher(PATH, q)
    watcher.run()

def communicator_thread(q):
    while True:
        filename = q.get()
        if filename is None:  # We can use None as a signal to terminate the thread
            break
        send_file(LOCALHOST, PORT, filename)
        time.sleep(3)

if __name__ == "__main__":
    q = Queue()

    t1 = threading.Thread(target=wachter_thread, args=(q,))
    t2 = threading.Thread(target=communicator_thread, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    q.put(None)  # Signal the communicator_thread to exit
    t2.join()

    # send_file(LOCALHOST, PORT, FILE)
