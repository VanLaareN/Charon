import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from socket_methods import PATH
from queue import Queue

class Watcher:
    def __init__(self, directory_to_watch, event_queue):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()
        self.event_queue = event_queue

    def run(self):
        event_handler = Handler(self.event_queue)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, event_queue):
        self.event_queue = event_queue

    def on_any_event(self, event):
        if event.is_directory:
            return None
        event_details = None
        if event.event_type == 'created':
            event_details = event.src_path
        elif event.event_type == 'modified':
            event_details = event.src_path
        elif event.event_type == 'deleted':
            event_details = event.src_path

        if event_details:
            print(event_details)
            self.event_queue.put(event_details)
