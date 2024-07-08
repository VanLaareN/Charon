from socket_methods import send_file, PATH
from observer import Watcher
import threading
from queue import Queue

LOCALHOST = 'localhost'
PORT = 12345

def watcher_thread(q):
    watcher = Watcher(PATH, q)
    watcher.run()

def communicator_thread(q):
    while True:
        filename = q.get()

        send_file(LOCALHOST, PORT, filename)

if __name__ == "__main__":
    q = Queue()

    t1 = threading.Thread(target=watcher_thread, args=(q,))
    t2 = threading.Thread(target=communicator_thread, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    q.put(None)  # Signal the communicator_thread to exit
    t2.join()
