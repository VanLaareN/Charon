import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from queue import Queue
from datetime import datetime

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
        self.processed_files = set()

    def on_modified(self, event):
        if event.is_directory:
            return None
        event_details = event.src_path
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        modified_event = event_details + str(time_stamp)
        if modified_event not in self.processed_files:
            self.processed_files.add(modified_event)
            self.event_queue.put(event_details)
